.PHONLY: play
play:
	ansible-playbook playbook.yml $(filter-out $@,$(MAKECMDGOALS))
