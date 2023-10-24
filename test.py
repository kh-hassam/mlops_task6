from main import Bulb

bulb = Bulb()

#Test Case-1
def test_bulb_isOff():
    assert bulb.getStatus() == "Bulb is not glowing"

#Test Case-2
def test_bulb_isOn():
    bulb.isOn()
    assert bulb.getStatus() == "Bulb is glowing"

#Test Case-3
def test_bulb_status():
    bulb.isOff()
    assert bulb.getStatus() == "Bulb is not glowing"

