# 3D Room Scanner

> Real-time 3D room capture system built on embedded hardware

![MSP432E401Y](https://img.shields.io/badge/MCU-MSP432E401Y-00FFB2) ![C](https://img.shields.io/badge/Language-C%20%28bare--metal%29-blue) ![Python](https://img.shields.io/badge/Language-Python-blue)

## Overview
A servo-mounted distance sensor sweeps a room in precise arcs, streaming thousands of polar-coordinate measurements over UART to a Python host, which converts them to 3D Cartesian coordinates and renders a live point cloud.

## Pipeline
`Servo sweep → ToF sensor → UART stream → Python parse → 3D render`

## Key Achievements
- Wrote bare-metal C firmware for MSP432E401Y — configuring GPIO, SPI/I²C, UART with no HAL abstraction
- Designed a full-stack embedded pipeline from sensor interrupt to Python 3D visualisation
- Applied polar-to-Cartesian transformation for accurate spatial reconstruction
- Managed real-time throughput within microcontroller memory constraints

## Tech Stack
| Layer | Technology |
|---|---|
| MCU | MSP432E401Y (ARM Cortex-M4) |
| Firmware | C (bare-metal) |
| Host software | Python (serial parsing, 3D rendering) |
| Comms | UART, I²C, SPI |

## Documentation
Full technical write-up in `/Project Report`
