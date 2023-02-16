import sys
sys.path.insert(0, '../../')
from typer.testing import CliRunner
from src.bulk import app

runner = CliRunner()


def test_bulk_command():
    result = runner.invoke(app, ['init'], input='das')
    assert result.exit_code == 0
    assert "['mysql', 'localhost', '3306', 'root', 'root', 'cli_test']" in result.stdout
    print(2312)



