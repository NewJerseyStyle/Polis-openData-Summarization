import re
import argparse

import pandas as pd
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

OPENDATA_OPTIONS = ['15-per-hour-seattle',
					'american-assembly.bowling-green',
					'brexit-consensus',
					'canadian-electoral-reform',
					'football-concussions',
					'march-on.operation-marchin-orders',
					'scoop-hivemind.affordable-housing',
					'scoop-hivemind.biodiversity',
					'scoop-hivemind.freshwater',
					'scoop-hivemind.taxes',
					'scoop-hivemind.ubi',
					'ssis.land-bank-farmland.2rumnecbeh.2021-08-01',
					'vtaiwan.uberx']

class Summarizer(object):
	"""docstring for Summarizer"""
	def __init__(self, model_name="csebuetnlp/mT5_multilingual_XLSum"):
		super(Summarizer, self).__init__()
		self.tokenizer = AutoTokenizer.from_pretrained(model_name)
		self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

	def summarize(self, conversation_topic, moderated_only=False):
		comments = self.get_comments(conversation_topic, moderated_only)
		article_text = '. '.join([str(comment) for comment in comments])
		
		WHITESPACE_HANDLER = lambda k: re.sub(
			'\s+', ' ', re.sub('\n+', ' ', k.strip()))

		input_ids = self.tokenizer(
			[WHITESPACE_HANDLER(article_text)],
			return_tensors="pt",
			padding="max_length",
			truncation=True,
			max_length=512
		)["input_ids"]

		output_ids = self.model.generate(
			input_ids=input_ids,
			max_length=84,
			no_repeat_ngram_size=2,
			num_beams=4
		)[0]

		summary = self.tokenizer.decode(
			output_ids,
			skip_special_tokens=True,
			clean_up_tokenization_spaces=False
		)

		return summary

	def get_comments(self, url_target, moderated_only=False):
		url =  ('https://raw.githubusercontent.com/'
				'compdemocracy/openData/master/'
				f'{url_target}/comments.csv')
		df = pd.read_csv(url, index_col=0)
		if moderated_only:
			mask = df['moderated'].values > 0
			# comments_moderated
			return df['comment-body'][mask].values
		# comments
		return df['comment-body'].values


def main(url_target, moderated_only):
	model = Summarizer()
	summary = model.summarize(url_target, moderated_only)
	print('========', 'conversation:', url_target, '========')
	print('summary of', 'moderated comments only' if moderated_only else 'all comments')
	print(summary)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(
		description='Summarization on Polis openData.')
	parser.add_argument('--conversation',
						choices=OPENDATA_OPTIONS + ['all'],
						help='Select and see what is the AI generated summary of the conversation',
						required=True)
	parser.add_argument('--only-moderated-comments',
						default=False, action='store_true',
						help=('Analysis only moderated comments,'
							  ' default False (i.e. Analysis all comments)'))
	args = parser.parse_args()

	if args.conversation == 'all':
		for conversation in OPENDATA_OPTIONS:
			for moderated in range(2):
				main(conversation, moderated)
	else:
		main(args.conversation, args.only_moderated_comments)
