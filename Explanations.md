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
- [Good reference](https://indico.cern.ch/event/9340/contributions/2121716/attachments/1102551/1572825/PM_workshop_-_Beam_dump_XPOC.pdf)

## Beam Setup Process

- The process of setting up for a physics beam starts with *SPS* injections at 450GeV
- Pilot injections are used to verify things like collimators and so on
- Once verified, a physics fill is injected
- The beam is then ramped up in intensity and energy, to a flat top
- The beams are then squeezed to the required beta*
- Collisions then commence

## Active Filling Scheme Format

`<bunch spacing>_<total bunches per beam>_<collisions at IP1/5>_<collisions at IP2>_<collisions at IP8>_<max bunches per injection>_<remarks>`

eg. `25ns_399b_386_266_278_48bpi_12inj_3INDIVs` means
- 25 ns bunch spacing
- 399 bunches total (per beam)
- IP1 and 5 get 386 collisions
- IP2 gets 266 collisions
- IP8 gets 278 collisions
- Maximum 48 bunches per injection
- 3 "individual" (ie. single-bunch) injections.

Generally, the first injection has 12 bunches rather than the full BPI, so the total bunches is usually something like

`(n - i - 1) * b + i + 12` 

where `n` is the number of injections, `i` is the number of INDIVs, and `b` is the listed max BPI. So in the above case:

`(12 - 3 - 1) * 48 + 3 + 12 = 399`

Newer VISTARS setup allows you to see the injection/bunch counts as they go in. Which is neat.

Excellent source for filling schemes and associated info is the [CERN LPC site](https://lpc.web.cern.ch), which has an [AFS viewer](https://lpc.web.cern.ch/cgi-bin/filling_schemes.py) and a [filling scheme editor](https://lpc.web.cern.ch/schemeEditor.html). The latter has a ton of info on how the fills are constructed: eg. "**pp physics:** A train of 12b (not colliding in IP1&5) is inserted at the beginning of the orbit (to steer the beams in the transfer lines)", which explains the above observation about the first injection on normal fills. Some other key points:

- Filling-scheme algorithm prioritises getting all bunches (after the 12b initial steering injection) to collide in IP1&5
- Its second priority is maximising collisions in IP8
- Maximal filling beyond this must be done by hand

To grab a JSON-formatted representation of a filling scheme, go to the [filling scheme editor](https://lpc.web.cern.ch/schemeEditor.html), enter `lpc` as the username, then click load, select from the tree structure, click save, select save locally, and you're sorted. Then you can use the python script in the `scripts` folder of this repo to view the filling.

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

## Scrubbing

- The LHC beamlines are not perfect vacuums
- The air molecules within can cause issues, since the protons will ionise those molecules, and the free electrons proceed to cause heating and pressure increases in the machine
- By sending low-energy protons through before a full-intensity run, they clean out the contaminants (leaving just inert graphite sticking to the machine walls)
- This is called "scrubbing"