from chaining import Chaining

chain_block = Chaining()

chain_block.append_block('tung')
chain_block.append_block('mai')
chain_block.append_block('thanh')
chain_block.append_block('what')

chain_block.view_meta()
print(chain_block.verify())
chain_block.get_block(2).message = 'heheh'
print(chain_block.verify())