.PHONLY: play
play:
	ansible-playbook playbook.yml $(filter-out $@,$(MAKECMDGOALS))

.PHONY: check
check:
	ansible-playbook -C --diff playbook.yml $(filter-out $@,$(MAKECMDGOALS))
