.PHONY: play
play:
	@ansible-playbook playbook.yml -i hosts $(filter-out $@,$(MAKECMDGOALS))

.PHONY: test-ci
test-ci:
	@ansible-playbook playbook.yml -i hosts --skip-tags "skip-ci"

.PHONY: check
check:
	@ansible-playbook -i hosts -C --diff playbook.yml $(filter-out $@,$(MAKECMDGOALS))

%:
	@:
