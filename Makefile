.PHONLY: play
play:
	@ansible-playbook playbook.yml -i hosts $(filter-out $@,$(MAKECMDGOALS))

.PHONY: check
check:
	@ansible-playbook -i hosts -C --diff playbook.yml $(filter-out $@,$(MAKECMDGOALS))

%:
	@:
