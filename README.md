# Summarization on Polis openData
This project is a tool demonstrating text summarization on comments of [Polis openData](https://github.com/compdemocracy/openData)

## Development started
Python3 (`>=3.8` recommended) `requirements.txt`:
```
transformer
sentencepiece
pytorch
protobuf
```

> :warning: For windows users downloading binary `protoc` and `protobuf-python` from [protobuf release page](https://github.com/protocolbuffers/protobuf/releases) is required to install `protobuf` form its Python source code `\protobuf-x.xx.x\python`. `pip install protobuf` does not give the latest package.
More installation instuctions refer to [protobuf documentation](https://github.com/protocolbuffers/protobuf/tree/main/python#installation)

## Test drive
```bash
python main.py --conversations american-assembly.bowling-green --only-moderated-comments
```

## Analysis all
```bash
python main.py --conversations all
```

## Results
|Conversation                                 |Comments |Summary   |
|---------------------------------------------|---------|----------|
|15-per-hour-seattle                          |All      |In our series of letters from African journalists, writer and columnist Adaobi Tricia Nwaubani explains why the minimum wage increase is a challenge.|
|15-per-hour-seattle                          |Moderated|In our series of letters from African journalists, writer and former chairman of the British Chambers of Industry, Tony Blair, considers whether the minimum wage should be raised.|
|american-assembly.bowling-green              |All      |Warren County's chief minister has announced a major shake-up of the county. Here is the full list of issues facing the city.|
|american-assembly.bowling-green              |Moderated|Nashville needs a new bypass to improve traffic flow.|
|brexit-consensus                             |All      |The Conservative Party's vote to leave the European Union was a "stupid idea" for the first time.|
|brexit-consensus                             |Moderated|The Conservative Party's vote to leave the European Union was a "stupid idea" for the first time.|
|canadian-electoral-reform                    |All      |Canadian Prime Minister Justin Trudeau says he wants to reform the electoral system in Canada. Here he explains what he thinks about his party.|
|canadian-electoral-reform                    |Moderated|Canadian Prime Minister Justin Trudeau says he wants to reform the electoral system in Canada. Here he explains what he thinks about his party.|
|football-concussions                         |All      |Football is a serious sport, but why should it be replaced by sports focusing more on cooparative aspects and social competences?|
|football-concussions                         |Moderated|Football is a sport populated by poorer people, but it will never fade because of its violent characteristics as long as we have guns, according to new research from the University of New York.|
|march-on.operation-marchin-orders            |All      |President Donald Trump has told the BBC how he wants to win the US elections.|
|march-on.operation-marchin-orders            |Moderated|US President Donald Trump says he wants a third party to be elected in the forthcoming US elections. Here is his statement.|
|scoop-hivemind.affordable-housing            |All      |New Zealand's housing crisis has led to the creation of a new generation of people living in the country. Here are some of the key recommendations.|
|scoop-hivemind.affordable-housing            |Moderated|New Zealand's housing crisis has led to a massive increase in the number of people buying their homes. Here is the full text of the proposals.|
|scoop-hivemind.biodiversity                  |All      |New Zealand's chief minister, Jacinda Ardern, has called on the public to give back to their indigenous species. Here, he describes the challenges facing the country.|
|scoop-hivemind.biodiversity                  |Moderated|New Zealand's chief minister, Jacinda Ardern, has called on the government to introduce a new strategy to protect indigenous species. Here is his proposal.|
|scoop-hivemind.freshwater                    |All      |The government has published a list of key recommendations for the future of the country's water quality.|
|scoop-hivemind.freshwater                    |Moderated|New Zealand's government has published a plan to tackle environmental pollution. Here is the full text of the plan.|
|scoop-hivemind.taxes                         |All      |New Zealand's government has announced a spending reduction of 7% in the last three years. Here is the full list of the savings.|
|scoop-hivemind.taxes                         |Moderated|New Zealand's economy is at its highest rate in almost two decades. Here is the full list of ways to tax people.|
|scoop-hivemind.ubi                           |All      |New Zealand's Prime Minister Jacinda Ardern has called on the government to introduce a higher income benefits system (ubi). Here he explains why.|
|scoop-hivemind.ubi                           |Moderated|New Zealand's Prime Minister, Jacinda Ardern, has called on the government to introduce a new Universal Independence Initiative (ubi).|
|ssis.land-bank-farmland.2rumnecbeh.2021-08-01|All      |The Labour Party (LB) has announced a raft of changes to its rules on the Isle of Man's Land Bank. Here is the full text of the decision.|
|ssis.land-bank-farmland.2rumnecbeh.2021-08-01|Moderated|The Isle of Man's Land Bank Commissioners have published their findings.|
|vtaiwan.uberx                                |All      |[我乘坐Uber,是一個叫派計程車的交通工具,我第一次聽到這個消息。](https://translate.google.com/?sl=zh-CN&tl=en&text=%E6%88%91%E4%B9%98%E5%9D%90Uber%2C%E6%98%AF%E4%B8%80%E5%80%8B%E5%8F%AB%E6%B4%BE%E8%A8%88%E7%A8%8B%E8%BB%8A%E7%9A%84%E4%BA%A4%E9%80%9A%E5%B7%A5%E5%85%B7%2C%E6%88%91%E7%AC%AC%E4%B8%80%E6%AC%A1%E8%81%BD%E5%88%B0%E9%80%99%E5%80%8B%E6%B6%88%E6%81%AF%E3%80%82&op=translate "I took Uber, a form of transportation, and it was the first time I heard about the news.")|
|vtaiwan.uberx                                |Moderated|[我的看法是:UberX應該合法化。](https://translate.google.com/?sl=zh-CN&tl=en&text=%E6%88%91%E7%9A%84%E7%9C%8B%E6%B3%95%E6%98%AF%3AUberX%E6%87%89%E8%A9%B2%E5%90%88%E6%B3%95%E5%8C%96%E3%80%82&op=translate "My opinion: UberX should be legalized.")|
