# --pdb: Invoke the debugger upon failure
# --pdbcls pudb.debugger:Debugger: Use the PUDB debugger
# --capture=no: let the debugger capture the IO
# --exitfirst: only debug the first failure, then end the tests
# --color=no: useful when debugging
.PHONY: help pudb ipython pdb clean

help:
	@echo Targets are: pdb, pudb, ipython, and clean

pudb:
	# Debug with pudb
	uv run pytest --log-cli-level=CRITICAL --pdbcls=pudb.debugger:Debugger --pdb --capture=no --exitfirst --color=no

ipython:
	# Debug with ipython
	uv run pytest --pdbcls=IPython.terminal.debugger:Pdb --pdb --capture=no --exitfirst --color=no

pdb:
	# Debug with the standard pdb
	uv run pytest --pdb --capture=no --exitfirst --color=no

clean:
	-rm -fr __pycache__
