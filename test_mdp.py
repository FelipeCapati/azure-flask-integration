def test_azure_flask_integration():
    ###########
    # Arranje #
    ###########
    x = 10
    y = 20

    ###########
    #   Act   #
    ###########
    z = x+y

    ###########
    #  Assert #
    ###########
    assert z == 30, "Test Failed"
