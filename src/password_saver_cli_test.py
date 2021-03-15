from click.testing import CliRunner
import password_saver_cli as cli

runner = CliRunner()

def test_cli_hello():
    result = runner.invoke(cli.hello)
    assert result.output == "Hello, this is password saver CLI 🛡\n"
    assert result.exit_code == 0
    
def test_cli_getPasswords():
    result = runner.invoke(cli.hello)
    assert result.output != None
    assert result.exit_code == 0