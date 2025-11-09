# ==============================
# Simple MANET Simulation
# ==============================

# Create simulator
set ns [new Simulator]

# Create trace and nam files
set tr [open manet.tr w]
set nf [open manet.nam w]
$ns trace-all $tr
$ns namtrace-all-wireless $nf 500 500

# Define topography and wireless setup
set topo [new Topography]
$topo load_flatgrid 500 500
create-god 2

# Configure nodes for wireless simulation
$ns node-config -adhocRouting DSDV \
                -llType LL \
                -macType Mac/802_11 \
                -ifqType Queue/DropTail/PriQueue \
                -ifqLen 50 \
                -antType Antenna/OmniAntenna \
                -propType Propagation/TwoRayGround \
                -phyType Phy/WirelessPhy \
                -channelType Channel/WirelessChannel \
                -topoInstance $topo

# Create two nodes
set n0 [$ns node]
set n1 [$ns node]

# Initial positions
$n0 set X_ 100; $n0 set Y_ 200; $n0 set Z_ 0
$n1 set X_ 300; $n1 set Y_ 200; $n1 set Z_ 0

# Define node movement
$ns at 1.0 "$n0 setdest 200 250 10"
$ns at 2.0 "$n1 setdest 250 250 10"

# Define finish procedure
proc finish {} {
    global ns tr nf
    $ns flush-trace
    close $tr
    close $nf
    exec nam manet.nam &
    exit 0
}

# End simulation
$ns at 5.0 "finish"

# Run simulation
$ns run

