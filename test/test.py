# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start")

    # Set the clock period to 10 us (100 KHz)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut._log.info("Reset")
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    dut._log.info("Test project behavior")

    # Nothing On
    
    # Set the input values you want to test
    # dut.ui_in.value = 20
    dut.ui_in.value = 0b00000000

    # Wait for one clock cycle to see the output values
    await ClockCycles(dut.clk, 1)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:
    assert dut.uo_out.value == 0b01001001
    
    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
    await ClockCycles(dut.clk, 5)

    # A14 on

    dut.ui_in.value = 0b00100000

    # Wait for two clock cycle to see the output values
    await ClockCycles(dut.clk, 2)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    assert dut.uo_out.value == 0b00101001

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
    await ClockCycles(dut.clk, 5)

    # cs clock only

    dut.ui_in.value = 0b00000001

    # Wait for two clock cycle to see the output values
    await ClockCycles(dut.clk, 2)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    assert dut.uo_out.value == 0b01101001

    # Keep testing the module by changing the input values, waiting for
    # one or more clock cycles, and asserting the expected output values.
    await ClockCycles(dut.clk, 5)

    # A14 & A15

    dut.ui_in.value = 0b00110000

    # Wait for two clock cycle to see the output values
    await ClockCycles(dut.clk, 2)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    assert dut.uo_out.value == 0b00111001
    await ClockCycles(dut.clk, 5)

    # A14 & cs_clk

    dut.ui_in.value = 0b00010001

    # Wait for two clock cycle to see the output values
    await ClockCycles(dut.clk, 2)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    assert dut.uo_out.value == 0b01110001
    await ClockCycles(dut.clk, 5)

    # A14 & ~15

    dut.ui_in.value = 0b00010000

    # Wait for two clock cycle to see the output values
    await ClockCycles(dut.clk, 2)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    assert dut.uo_out.value == 0b01010001
    await ClockCycles(dut.clk, 5)


    # A14 & A13

    dut.ui_in.value = 0b00011000

    # Wait for two clock cycle to see the output values
    await ClockCycles(dut.clk, 2)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    assert dut.uo_out.value == 0b01010101
    await ClockCycles(dut.clk, 5)

    # A14 & A12

    dut.ui_in.value = 0b00010100

    # Wait for two clock cycle to see the output values
    await ClockCycles(dut.clk, 2)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    assert dut.uo_out.value == 0b01010011
    await ClockCycles(dut.clk, 5)

    # A14 & A11

    dut.ui_in.value = 0b00010010

    # Wait for two clock cycle to see the output values
    await ClockCycles(dut.clk, 2)

    # The following assersion is just an example of how to check the output values.
    # Change it to match the actual expected output of your module:

    assert dut.uo_out.value == 0b01010000
    await ClockCycles(dut.clk, 5)