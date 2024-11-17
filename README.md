# EPIC-Showcase-Night-2024



# Wiring Your Circuit


## Gather Your Materials
![Screenshot from 2024-11-17 12-51-34](https://github.com/user-attachments/assets/92a0354c-0fee-4e02-8b68-4b9d2c160e9c)

You will need 
- (1) Breadboard connected to your Pi by a T-cobbler
- (2) M-M jumper wires
- (1) 5mm Light Bulb
- (1) Resistor


## Create Your Circuit 

### Overview and Vocabulary

![Screenshot from 2024-11-17 13-29-34](https://github.com/user-attachments/assets/66ee4bf9-5b2d-4c5b-a964-501fd7b37b9a)

In order to create a circuit to turn on our light using Python, we will need to take advantage of our Rapsberry Pi's **GPIO**(general purpose input-output) pins. Some of the pins can be turned on and off using Python, which is how we will power our light.

Right now, your Pi already is connected to a **breadboard** using a **T-cobbler**. A breadboard allows us to quickly create circuits with M-M wires instead of soldering.

![Screenshot from 2024-11-17 13-07-05](https://github.com/user-attachments/assets/b3ccfba8-1569-4169-9062-6f1d078e09ad)

To connect a wire to another wire using a breadboard, plug the two wires into the same **rail** or horizontal row on the board. _Note: the horizontal rails of the breadboard are not connected across the gap in the middle or to either of the colored vertial rails on each side._

When our circuit is complete, we want it to look something like this: 

![Screenshot from 2024-11-17 13-23-48](https://github.com/user-attachments/assets/c71945e4-6e6b-4d4d-b5fb-ae7357abd337)

### Wiring Walkthrough

Let's work left to right connected all of the components in the diagram above. **Complete these steps with the Pi off!**

#### Step 1 - Connect to GPIO Pin 18

Plug one end of one of your jumpter wires into the same row on your breadboard as pin 18. _Use the numberering on the blug T-cobbler, not the breadboard._

![Screenshot from 2024-11-17 13-42-08](https://github.com/user-attachments/assets/be8c56c4-3be9-474f-8444-4a3f6dcd2f5a)

#### Step 2 - Plug the Other End of the Wire into an Empty Rail 

Connect the other end of the wire you just connected to Pin 18 into an empty rail of the breadboard. **DO NOT** put it in the same row as any other piece of your blue T-cobbler.

![Screenshot from 2024-11-17 13-46-06](https://github.com/user-attachments/assets/c3dbc492-0efc-40cd-8c0e-438b02b7b37f)

#### Step 3 - Connect the Long End of Your Light to this Wire

Put the long end of your lightbulb into the same row as the wire in step 2. **DO NOT** put the other end of the lightbulb in the same row, put it in an adjacent row. Push down on the LED to make sure it is actually in the breadboard. You may need to apply a little bit of force. 

![Screenshot from 2024-11-17 13-23-58](https://github.com/user-attachments/assets/539e3d84-df6e-465a-bd67-a0ff72b6015a)



on the Raspberry Pi. In order to create a 




