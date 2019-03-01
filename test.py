# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:31:14 2019

@author: Admin
"""

from ethjsonrpc import EthJsonRpc

#This is a direct implementation from test.py in github repisotory


methods = [
    'web3_clientVersion',
    'net_version',
    'net_peerCount',
    'net_listening',
    'eth_protocolVersion',
    'eth_syncing',
    'eth_coinbase',
    'eth_mining',
    'eth_hashrate',
    'eth_gasPrice',
    'eth_accounts',
    'eth_blockNumber',
    'eth_getCompilers',
    'eth_newPendingTransactionFilter',
    'eth_getWork',
#    'shh_version',
#    'shh_newIdentity',
#    'shh_newGroup',
]

c = EthJsonRpc()
print (len(methods))
for m in methods:
    meth = getattr(c, m)
    result = meth()
    print ('%s: %s (%s)' % (m, result, type(result)))

################################################################################
print ('*' * 80)

addr = '0x9b6f69dff31d28bad4f5e269916c8b0762e8b7c8' #adding Address given in email

b = (7285499, '0x9e06be2fc85c95f373c10932e976dd9c8c06d279df4f9cef294ba317ca3291ae')
result = c.eth_getBlockTransactionCountByHash(b[1])
print ('eth_getBlockTransactionCountByHash: %s (%s)' % (result, type(result)))
#The code above should print 0.04979 (Ether)

b = (7284960, '0x99f4f2690cdcb0a6404dc098f82582cc0f8892e38a6c424fdffe5e52d84de40c ')
result = c.eth_getBlockTransactionCountByHash(b[1])
print ('eth_getBlockTransactionCountByHash: %s (%s)' % (result, type(result)))
#The code above should print 0.46379 (Ether)
################################################################################
print ('*' * 80)