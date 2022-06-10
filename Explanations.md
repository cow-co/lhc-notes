# More In-Depth Explanations

## Injections

- The LHC beams originate in the *LINAC*s (LINear ACcelerators)
- The beams cannot be continuous, since there must be gaps to allow kicker magnets (the magnets which transfer the beam from one line to another) to rise to full strength
- Therefore, there is a bunch --> batch --> injection --> fill structure
- The *LINAC* generates *bunches* of protons
- The bunches are grouped into a *batch*. The bunches in a batch are separated by (now) 25ns, though it used to be 50ns - this is the rise time of the kickers from the *LINAC* to the *PSB*
- The batches are then formed (with gaps between them of somewhere in the region of 250ns) into an injection, to the *SPS*
- The injections are then sent to the LHC, with gaps between them of about 900ns
- If multiple fills are needed, then they must be separated by the abort gap (~3μs) 

## Beam Dump

- The beams are highly energetic, and can generate intense radiation on impact with materials
- As such, it is imperative that they can be stopped safely
- This is the purpose of the beam dump system
- Beam dump starts with *MKD*s kicking the beam out horizontally
- The *MSD* then shifts the beam vertically
- The beam now goes through a series of horizontal and vertical magnets, which spin the beam out in an "e" shape
- The beam width itself also widens
- The beam travels through a roughly 600m-long straight tunnel
- The beam then impacts a multiple-metre-long solid block of graphite, encased in a steel container
- The impact point heats to between 1000-1500 Celsius (depending on which Run we're looking at)
- People aren't allowed in, because of the immense radiation generated, but if they were then they'd hear a very loud bang/bell noise of the rapid thermal expansion/contraction of the dump target materials
- The dump targets have become so radioactive that, instead of removing them to be replaced, the LHC engineers are simply using the spares as the new HL-LHC dump targets and leaving the old ones be 

## Beam Setup Process

- The process of setting up for a physics beam starts with *SPS* injections at 450GeV
- Pilot injections are used to verify things like collimators and so on
- Once verified, a physics fill is injected
- The beam is then ramped up in intensity and energy, to a flat top
- The beams are then squeezed to the required beta*
- Collisions then commence

## Active Filling Scheme Format

`<# of injections>_<# of bunches per injection>_<# of collisions IP1/5>_<# of collisions IP2>_<# of collisions IP8>_<remarks>`

eg. `Single_42b_0_0_0_noHOnoLR` means
- One injection
- 42 bunches
- No collisions at any of the *IP*s
- No head-on, no long-range(?)

## Circuit Naming Convention

- There are a lot of circuits in the LHC (thousands!)
- But most of the ones you'll see mentioned follow a broad convention which can be summarised as

`<circuit type>.<part of machine>.<optional subpart>`

- For example: `RB.A78.UA83` means
  - Main bending-dipole circuit - the `RB`
  - Arc 78 (between points 7 and 8) - the `A78`
  - Power converter in UA83 - the `UA83`

## Magnets, Arcs, LBBs, LSS, DSR, DSL, oh my!

- The LHC comprises eight arcs and eight long straights
- The machine is split into eight quadrants, which extend between arcs
  - ie. An octant goes from halfway along one arc, to halfway along the next arc
- The octant comprises:
  - (half of) an arc
  - A *DSL* (Dispersion Suppressor Left)
  - An *LSS* (Long Straight Section)
  - A *DSR* (Dispersion Suppressor Right)
  - (half of) the next arc
- The arcs themselves comprise 23 cells each.
- Each cell comprises two half-cells
- Each half-cell comprises:
  - Three bending dipoles (the *MB*s)
  - One quadrupole magnet (these alternate as focusing, then defocusing)
  - Other correction magnets