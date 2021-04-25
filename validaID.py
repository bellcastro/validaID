# -*- coding: utf-8 -*-
def validaID (id):
    especiais = "[^-áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ:]#*.,!@#$%¨&*()_{^}<>/º°"
    if len(id) > 0 and len(id) < 7:
        try:
            int (id[0])
        except ValueError:
            novo_id = id
            for x in especiais:
                novo_id = novo_id.replace(x, '')
            if novo_id == id:
                return True
    return False
  
