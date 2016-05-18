# Считывает инструкции
def read_inst(instructions_number):
	# Словарь инструкций, будет в следующем виде:
	# {q0:{v1:(q v d), v2:(q v d), ...}, q1:{v1:(q v d), ...}, ...}
	inst_dict = {}
	
	file = open('inst_'+ instructions_number +'.txt')
	string = file.readline().rstrip()
	while string:
		# Начальное состояние, начальное значение, конечное состояние, конечное значение, направление (влево/вправо)
		init_state, init_value, end_state, end_value, direction = string.split()
		if init_state in inst_dict:
			inst_dict[init_state].update({init_value:(end_state, end_value, direction)})
		else:
			inst_dict.update({init_state:{init_value:(end_state, end_value, direction)}})
		string = file.readline().rstrip()
	file.close()
	return inst_dict

# Считывает начальные данные
def read_init(init_data_number):
	file = open('init_'+ init_data_number +'.txt')
	string = file.readline().rstrip()
	init_state, init_position = string.split()
	init_position = int(init_position)
	string = file.readline().rstrip()
	line = string
	file.close()
	return init_state, init_position, line
	
inst_dict = read_inst(input("Instruction's Number: "))
init_state, pos, line = read_init(input("Iniial Data's Number: "))
ch_line = list(line) # Переводим строку в массив - изменяемый объект

while init_state != 'Q': # Q - конечное состояние
	init_value = ch_line[pos]
	if init_state in inst_dict:
		if init_value in inst_dict[init_state]:
			
			cortege = inst_dict[init_state][init_value]
			end_state, end_value, direction = cortege[0], cortege[1], cortege[2]
			ch_line[pos] = end_value
			
			if direction == 'R':
				pos += 1
			else:
				pos -= 1
			
			init_state = end_state
		
		else:
			print("Value isn't exist:", init_value, 'in', init_state, inst_dict[init_state])
			break
	else:
		print("State isn't exist:", init_state, inst_dict.keys())
		break
ch_line = ''.join(ch_line) # Переводим массив обратно в строку
print(line, ' -> ', ch_line)