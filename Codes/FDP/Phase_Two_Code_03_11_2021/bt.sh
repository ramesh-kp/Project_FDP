#!/bin/bash

bluetoothctl << EOF

power on

discoverable on

agent on

default-agent

pairable on

EOF