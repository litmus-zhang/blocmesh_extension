from extension_test import main


def test_get_message_from_extension(capsys):
    main.get_message_from_extension()
    captured = capsys.readouterr()
    assert captured.out == "Stored value: Hello world!\n"
