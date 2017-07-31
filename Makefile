.PHONLY: play
play:
	ansible-playbook -i hosts playbook.yml $(filter-out $@,$(MAKECMDGOALS))

.PHONY: check
check:
	ansible-playbook -i hosts -C --diff playbook.yml $(filter-out $@,$(MAKECMDGOALS))
