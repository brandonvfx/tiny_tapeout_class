/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_6502_chip_select (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  reg [7:0] data_out;

  // All output pins must be assigned. If not used, assign to 0.
  assign uio_out = 0;
  assign uio_oe  = 0;

  wire cs_clk = ui_in[0];
  wire A11 = ui_in[1];
  wire A12 = ui_in[2];
  wire A13 = ui_in[3];
  wire A14 = ui_in[4];
  wire A15 = ui_in[5];

  wire peripheral_select = (~A15 & A14);
  // put your logic here, e.g.:
  always @ (posedge clk) begin
    data_out[7] <= 0;
    data_out[6] <= ~A15;
    data_out[5] <= ~(~A15 & ~cs_clk);
    data_out[4] <= A14;
    data_out[3] <= ~peripheral_select;
    data_out[2] <= peripheral_select & A13;
    data_out[1] <= peripheral_select & A12;
    data_out[0] <= ~(peripheral_select & ~A13 & ~A12 & A11);
  end

  assign uo_out = data_out;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, ui_in[6], ui_in[7], uio_in, rst_n, 1'b0};

endmodule
