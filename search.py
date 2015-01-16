import pyelasticsearch as pyes

keyword = '張世瑛'

es = pyes.ElasticSearch('http://localhost:9200')

# query = {'query':{'match':{'message':'資訊部'}}}
# query = {'query':{'match_phrase':{'message':'資訊部'}}}
# query = {'query':{'match_phrase':{'comments.data.message':'鄧美玉'}}}

# query = {
#     'filtered':{
#         'query':{
#             'multi_match':{
#                 'type':'phrase',
#                 'query':keyword,
#                 'fields':['comments.data.message','message']
#             }
#         },
#         'filter':{
#             'and':[
#                 {'match_phrase':{'message':'會計學'}},
#                 {'match_phrase':{'message':'鄧美玉'}}
#             ]
#         }
#     }
# }

query = {'query':{'multi_match':{'type':'phrase','query':keyword,'fields':['message','comments.data.message']}}}

result = es.search(query, index = 'ntustask', doc_type = 'ntusttalktalk', size = 100)
for row in result['hits']['hits']:
    print('======')
    print((row['_source']['message']))
    print((row['_source']['id']))

result = es.count(query, index = 'ntustask', doc_type = 'ntusttalktalk')
print('出現次數：' + str(result['count']) + '次')

# for k in keyword:
#     query = {'query':{'multi_match':{'type':'phrase','query':k,'fields':['message','comments.data.message']}}}
#     print('關鍵字：' + k)
#     result = es.count(query, index = 'ntustask', doc_type = 'ntusttalktalk')
#     print('出現次數：' + str(result['count']) + '次')
#     print('--')
