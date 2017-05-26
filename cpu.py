
class Chip8:

    def __init__(self):
        print("Starting up Chip8...")

        # index register for V
        self.I = 0

        # program counter for indexing into memory
        self.pc = 0

        # 15 general purpose registers and 1 carry flag
        self.V = []

        # 4096 bytes of memory
        # read this in from file path passed into instance
        self.memory = []

        # set up graphics somehow
        self.gfx = []

        self.delay_timer = 0
        self.sound_timer = 0

        # stack for subroutine calls, use stackpointer to hold pc
        self.stack = []
        self.sp = 0

        # hex based keypad 0x0-0xF to store the current state
        self.key = []

    def start():
        # set up graphics somehow
        while True:
            emulate_cycle()

        # if draw flag set, update graphics

    def emulate_cycle():

        pass


    def clear_display():
        # 00E0 clears the screen
        pass

    def return_from_subroutine():
        # 00EE duh
        pass

    def jump_to_address():
        # 1NNN jumps to address
        pass

    def call_subroutine_at_address():
        # 2NNN calls subroutine at NNN
        pass

    def skip_instruction_if_reg_equal():
        # 3XNN skips next instruction if VX equals NN
        pass

    def skip_instruction_if_reg_not_equal():
        # 4XNN skips next insturction if VX doesn't equal NN
        pass

    def skip_instruction_if_reg_equal_reg():
        # 5XY0 skips next instruction if VX equals VY
        pass

    def set_reg_to_value():
        # 6XNN sets VX to NN
        pass

    def add_value_to_reg():
        # 7XNN adds NN to VX
        pass

    def set_reg_to_reg():
        # 8XY0 sets VX to value of VY
        pass

    def bitwise_or():
        # 8XY1 sets VX to VX|VY, VF reset to 0.
        pass

    def bitwise_and():
        # 8XY2 sets VX to VX&VY. VF reset to 0
        pass

    def bitwise_xor():
        # 8XY3 sets vx to VX^VY. VF is reset to 0
        pass

    def add_equals():
        # 8XY4 sets VX to VX + VY. VF is set to 1 when theres a carry bit, 0 otherwise
        pass

    def subtract_equals():
        # 8XY5 VX = VX - VY. VF is set to 0 when theres a borrow, 1 otherwise
        pass

    def bitwise_right_shitf():
        # 8XY6 shifts VX right by one. VF set to least significant bit of VX before shift
        pass

    def subtract_reg1_from_reg2():
        # 8XY7 VX = VY - VX. VF set to 0 when theres borrow, 1 otherwise
        pass

    def bitwise_left_shift():
        # 8XYE Shifts VX left 1. VF set to most significant bit of VX before the shifts
        pass

    def skip_instruction_if_reg_not_equal_reg():
        # 9XY0 skip next insturction if VX != VY
        pass

    def set_index_to_address():
        # ANNN set I to NNN
        pass

    def jump_to_address_plus_offset():
        # BNNN pc=V0+NNN
        pass

    def set_reg_to_bitwise_and_of_randon():
        # CXNN VX=rand()&NN. typically randon between 0 and 255
        pass

    def draw_sprite():
        # lookup when ready
        pass

    def skip_instruction_if_key_pressed():
        # EX9E skips instruction if the key sotred in VX is pressed
        pass

    def skip_instruction_if_key_not_pressed():
        # EXA1 skips instruction if they key stored in VX not pressed
        pass

    def get_delay_timer():
        # FX07 VX=delay_timer. Blocking operation. all instructions halted until next key event.
        pass

    def get_key_pressed():
        # FX0A VX=get_key(). blocking operation.
        pass

    def set_delay_timer():
        # FX15 set delay_timer=VX
        pass

    def set_sound_timer():
        # FX18 sound_timer = VX
        pass

    def index_plus_equals_reg():
        # FX1E adds I=I+VX
        pass

    def set_index_to_sprite_location():
        # FX29 i=sprite_addr[VX]
        pass

    def set_binary_coded_decimal():
        # FX33
        pass

    def store_registers_in_memory():
        # FX55 store V starting at address I
        pass

    def load_registers_from_memory():
        # FX65 fills V with values from memory starting at index
        pass






if __name__ == "__main__":
    # parse command line argument and pass into Chip8 instance
    chip8 = Chip8()
