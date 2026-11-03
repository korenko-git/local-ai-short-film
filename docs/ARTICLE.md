# Generating a short film locally

How a four-minute birthday film turned into a three-day adventure with Codex, ComfyUI and a GPU with 16 GB of VRAM.

My production diary · Dmytro Korenko

I wanted to make a personal birthday film: an island, a pirate dossier, a shaky bridge, an ancient water puzzle and a talking parrot. Getting the images was only the beginning. The real work was keeping the character recognizable, making the actions understandable and turning separate generations into one continuous story.

The useful outcome was a repeatable process: direct an action, check connected keyframes, generate manageable shots, then fix the rhythm from preserved materials. The last changes needed a new edit rather than a fresh round of slow video rendering.

4:10 v3 assembly · 12 scenes · 24 frames per second · 16 GB GPU memory

<a id="models"></a>

## A fast first attempt, then a much better image

My first video attempt used Wan 2.2. It was quick, but that older model’s result looked terrible to me for this project. The sound was usable; the picture and action were not. Switching to MiniMax H3 through FreeVideo made a major difference, especially in close-up detail. That improvement came with much longer waits, and it still depended on good keyframes.

What I used

| Task | Tool | Role |
| --- | --- | --- |
| Keyframes | Qwen Image 2.1 | The main model for keyframes. |
| Some puzzle images | GPT Image | Alternative states and corrections in trial three. |
| Intelligible speech | Drama 3 | Consistent voices, short lines, pauses and performance. |
| Video | MiniMax H3 / FreeVideo | Motion, camera movement and environmental sound. |
| Orchestration and editing | Codex, ComfyUI MCP, FFmpeg | Workflows, inputs, run records, sound mixing and assembly. |

Most image, speech and video generation ran on my own PC. The exception was some of the water-puzzle keyframes, for which I used GPT Image through an external service.

MiniMax H3 is the model; FreeVideo is the local inference tool I used to run it. Its documentation describes the VDN-H3 work from OpenVDN and Video DeltaNet. In this project I called FreeVideo through its CLI, while Qwen and Drama ran in local ComfyUI workflows through MCP.

Codex and ComfyUI MCP saved me a lot of manual setup. The agent found installed models, worked out how to use them, prepared workflows, connected nodes and kept the outputs organized. I still had to direct the scene and reject bad results. Many of the most useful instructions were specific observations: the river is frozen, the rope goes the wrong way, the character has not actually touched the sign.

<a id="memory"></a>

## 16 GB of VRAM, and about 52 GB of system RAM

PC configuration

| Component | Specification |
| --- | --- |
| Graphics card | NVIDIA GeForce RTX 5070 Ti |
| Video memory | 16 GB VRAM |
| Processor | AMD Ryzen 7 9800X3D |
| System memory | 64 GB RAM |

During one speech-generation run, occupied system memory reached roughly 52 GB. That was the total RAM in use on my system at that moment, rather than an isolated measurement of the model’s consumption. The graphics card has its own memory: 16 GB of VRAM.

Other developers’ work made this practical. FreeVideo coordinates weights across VRAM, RAM and disk using techniques such as weight streaming, prefetching and chunked computation. My setup used its prepared int8 ConvRot cache. Qwen’s model and text encoder also used int8 ConvRot weights, while the installed Drama variant was named w4a8experts_bf16. Ready-made inference engines, compressed weights and ComfyUI integrations were essential parts of the pipeline.

I was building on the model developers’ work, OpenVDN and Video DeltaNet, FlashML-org’s FreeVideo, ComfyUI, PedroMarinhoDev’s Drama integration and the MCP tools. The agent helped connect those pieces. It did not invent the memory optimizations.

Speech generated relatively quickly even on the CPU. In my working setup, video took about a minute and a half per second of output at 24 fps. The basic settings were 1344 × 768, one pass and 16 steps. A ten-second test could mean fifteen minutes of waiting. A bad keyframe was expensive, so reviewing connected images before starting the video paid off.

<a id="pipeline"></a>

## The folder structure became the film’s memory

My early results exposed the difference between a description and a scene. There was too little action, the trials barely read, and the chest kept changing. I started treating every sequence as a set of shots: establish a problem, show the reaction, show the physical action, then its result. Reviewing each stage mattered more than making the prompt longer.

Once experiments started piling up, I organized the project around scenes and clips. Each scene got its own images, source video, voice lines, effects, workflows and edit. Shared faces, costume, voices and music lived separately. That helped the agent return to the same character and props instead of reinventing them.

> Story → connected keyframes → review → speech and video → edit → review

I kept each shot’s prompt, media.json, input images, seed and generation parameters next to its task. The scene README recorded results, feedback, versions, approvals and remaining work. A main index tracked the whole story. A render finishing was different from me accepting it; an interrupted attempt did not become a finished clip.

```
scenes/
  README.md                  story and current status
  NN-scene-name/
    README.md                decisions and scene journal
    frames/                  connected keyframes
    video/raw/               original generations
    video/drafts/rejected/   rejected attempts
    audio/voice/             dialogue
    audio/sfx/               precise effects
    workflows/               prompts, inputs, seeds, settings
    output/                  current complete scene
      clips/                 copies of accepted clips
    work/archive/            superseded edits
shared/                      common identity, voices, music
output/assemblies/           full-film assemblies
```

I kept originals in video/raw, copies of accepted clips in output/clips and only one current complete scene in the root of output. Previous full edits went to work/archive. Some transitions used the actual last frame of the previous clip, including the move away from the chest toward the night-time cliff.

<a id="edit"></a>

## Editing by GPT Luna

I entrusted the editing to GPT Luna, the model I used in the Codex agent for video work. I described the changes I wanted, and Luna prepared and ran FFmpeg commands and Python scripts: trimming and joining clips, aligning sound with the picture, freezing selected areas of a frame and adding graphic overlays. These changes used the existing material, so they did not require another video generation.

### How Luna reviewed generated video

After generation, Luna checked the result before editing. It used FFmpeg to extract one frame per second, resize the frames to 448 × 256 and assemble them into a 4 × 2 contact sheet. This put the sequence of actions in one image: the character’s location, changing pose and whether the intended action actually happened. It checked the file duration with ffprobe. In the example below, the clip lasted 6.58 seconds; seven frames filled seven cells, leaving the last empty.

![Scene 7 review contact sheet · Seven frames from a 6.58-second clip, sampled at one frame per second.](../article/assets/luna-video-review-contact.jpg)

Scene 7 review contact sheet · Seven frames from a 6.58-second clip, sampled at one frame per second.

When a result had an obvious error, Luna could reject it and restart generation on its own. That happened with the run in scene nine: instead of transferring the movement, the video guide pulled the result toward anime. Luna wrote in the production chat:

> “This version does not work: the video-guide mode almost copied the anime… I’m rejecting it.”

It then restarted the task using images of the character and corridor. The video reference became a staging guide translated into written direction: a close-up with speed lines, a camera move around to the side and running with sparks. This preserved the intended movement without copying the anime character.

Full breakdown and final clip: [Directing speed from a motion reference](#speed-reference).

### Static text over a looping animation

The dossier video was about 9–10 seconds long, while the voice-cloned narration lasted 20 seconds. To keep the picture running until the recording ended, the short animation had to loop. That also restarted the text reveal: the lettering disappeared and appeared again. Luna quickly solved the problem by cropping the area with the fully revealed text from the last frame and holding it over the video while the character animation continued moving. The result reminded me of photographs in Harry Potter, where the people in the pictures repeat their movements.

![An illustrated character in a pirate personnel dossier](../article/assets/dossier.jpg)

00:25 · The illustrated dossier is a deliberate exception to the film’s photorealistic world.

### Cuts and editing rhythm

Using the same keyframe at the end of one clip and the start of another preserved the composition but sometimes created a noticeable pause. Luna trimmed repeated poses and moved the dialogue and achievement overlays along with the edit. It also moved the narrator’s line about the failed attempt to a point on the timeline after the wrong turn had actually happened.

The last edit notes

| Problem | Change |
| --- | --- |
| Bridge reward too early | Move it to the landing at 1:10. |
| Holds at puzzle joins | Trim duplicate poses in trials two and three. |
| Long freeze by the wheel | Remove another 2.5 seconds in v3. |
| Parrot cut too aggressively | Restore the flight and reaction: +1.75 seconds. |
| Waiting after packing | Remove 2.25 seconds before the departure. |
| Extra first-ride shot | Remove it before the birthday ending. |

Assembly v2 ran for 253.2 seconds; v3 for 250.3. A few seconds matter when the character seems to be waiting for the next clip to start.

### One achievement template, four trials

The achievement graphics were a pleasant surprise. GPT Luna created a shared SVG template with a medallion, frame, colours and type. For each trial, it filled in the title and number while keeping the design consistent. The graphics were added during editing, so the wording, screen position and timing could change without another video generation.

![Example from GPT Luna’s shared SVG template: the first trial’s achievement. The text stays Russian, as it is in the film.](../article/assets/achievement-example.svg)

Example from GPT Luna’s shared SVG template: the first trial’s achievement. The text stays Russian, as it is in the film.

[SVG template](../article/assets/achievement-template.svg) · [Python renderer](../article/assets/render_trial_achievement.py)

Beside the template is render_trial_achievement.py. The script takes the trial number, title and total count, validates the number and adjusts the title font size to fit. It saves an SVG with those values filled in, then draws a separate transparent PNG with Pillow, first at twice the resolution and then down to 400 × 92. That PNG can be overlaid on video with FFmpeg.

![A courage achievement graphic over the completed bridge trial](../article/assets/bridge-achievement.jpg)

01:11 · The overlay appears after the bridge landing, independently of the source footage.

Originally the courage badge appeared before the character had crossed. Luna moved it to the landing, around 1:10 of the full film. The same separation made it easy to change the trial count to four while keeping the design consistent.

<a id="voice"></a>

## A performance assembled from several attempts

To keep voices consistent across scenes, I used shared voice references and saved each scene’s actual lines beside its footage. The narrator, short character lines and parrot used their own established references. Drama 3’s expressive tags, pauses and pronunciation choices made a substantial difference.

For the dossier, I supplied a recording with a cloned voice and a ticking-clock sound, then added sea ambience.

For the parrot I wanted a rolled ‘r’, a pause after the cannons and an excited finish. One attempt had a wonderfully inarticulate opening cry; another was cut off. I combined the first two seconds of the early cry with a later spoken version, removing its first half-second. The accident became a character moment: the chest opens, the parrot wakes with a squawk and launches into its rehearsed speech.

FreeVideo could supply useful sea, foliage, birds and sometimes music together with the picture. I used Drama 3 for intelligible speech. In the speed sequence, the video model added nonsense voices, so the sound needed further editing. Precisely timed cracks, impacts and mechanism sounds could be separate effects.

Not all the audio was generated. Early scenes used Kevin MacLeod’s Adventures in Adventureland, and the sea ambience came from Joseph Sardin / BigSoundBank. I kept the source and licensing records with the project; the attribution is also included below.

<a id="details"></a>

## Successful moments

### Two camera changes that mattered

The second clip of the bridge trial is an orbit around the character and the bridge. It reveals the valley’s depth and the height of the crossing ahead. The camera movement helps convey the danger.

[The second bridge clip: an orbit that reveals the drop.](../article/assets/bridge-camera.mp4?raw=true)

The second clip of the curiosity trial does a different job: it changes the view to show the blocked path from the character’s perspective. Showing the empty dead end before the character enters gives the viewer a chance to understand the problem. This was more useful than cutting straight to someone standing beside a sign.

[The second clip of trial two: establishing the dead end from a new viewpoint.](../article/assets/curiosity-camera.mp4?raw=true)

### Wind in the hair

In scene four, while the character receives the map on deck, the hair moves in the wind. It is a tiny detail, but I immediately noticed it. Along with the sea behind the ship, that movement makes the location feel like an actual breezy deck rather than a portrait pasted onto a background.

[Scene 4 · Watch the hair move in the sea breeze while the character unfolds the map.](../article/assets/hair-wind.mp4?raw=true)

### Taking things out of the chest

I liked how MiniMax handled the character collecting the gift. Hands, lid, clothing, scooter and helmet needed to interact within one scene. First I replaced an unconvincing keyframe in which the chest seemed to open by itself; the character now held its lid. Later he actually took the things with him.

![The character lifting the folded scooter in its case from the chest](../article/assets/belongings.jpg)

03:33 · The character physically takes the gift out of the chest.

### The parrot was a highlight

The parrot turned out particularly well. I made a separate video insert in which its beak tries to move with a human pirate line. Drama 3 provided the clear speech; the video supplied the performance. The synchronization is imperfect, but the parrot is convincing, as though it were repeating a memorized phrase.

![A close-up of the parrot speaking beside the chest](../article/assets/parrot.jpg)

03:24 · Beak movement and a separately generated human voice create the performance.

<a id="speed-reference"></a>

### Directing speed from a motion reference

For the fourth trial I wanted more than a run toward a gate. I brought in an anime reference for expressive camera turns, background blur and sparks beneath the shoes. I asked for the camera to come around from behind to a side profile, with the reference’s close-up and speed lines at the beginning. The contact sheet below shows the visual rhythm I was borrowing.

![Anime motion-reference contact sheet showing facial close-ups, speed lines, low running angles and sparks](../article/assets/speed-reference.jpg)

Motion reference · Contact sheet from the anime clip I supplied during production. These are reference frames, not generated shots from my film.

An early attempt fed the whole clip directly as a video guide and copied too much: the result brought over the anime look and another character. The successful version used only image references of my character and the corridor. The full motion reference was translated into written staging: a surprised close-up with streaks above and below, rear tracking, a move to the side, blurred walls and golden sparks around the shoes. FreeVideo generated the streaks and sparks inside the shot.

[Accepted speed insert v5 · 6.58 seconds, rear-to-side camera movement, generated streaks/sparks, retained music and the revised Russian cue.](../article/assets/speed-dynamic.mp4?raw=true)

<a id="artifacts"></a>

## Generation artifacts

### A map for the viewer rather than the character

At 00:50–00:52 the character seems to read the map, but its drawing faces the viewer. Without a dedicated keyframe for that action, the video model posed the character as though he were presenting a prop to the camera. At 03:01–03:03 the mistake returns, and the map itself differs from the one at the beginning. I should have made a shared reference for the map and other important props and reused it across scenes.

![00:50–00:52 · The map faces the viewer although the character is supposed to read it.](../article/assets/artifact-map-early.jpg)

00:50–00:52 · The map faces the viewer although the character is supposed to read it.

![03:01–03:03 · The pose repeats, but the map’s drawing and shape have changed.](../article/assets/artifact-map-late.jpg)

03:01–03:03 · The pose repeats, but the map’s drawing and shape have changed.

### The bridge keyframe: references helped, but did not fix everything

The agent first tried to make the keyframe with local Qwen. Instead of a test of courage, it produced safe-looking bridges: a short crossing almost at ground level, or a sturdy wooden structure with solid railings. Even once a deep valley appeared, the bridge itself looked too substantial. Replacing the timber rails with ropes still did not give it the precarious feel I wanted.

![Early Qwen attempt · A short bridge above a shallow stream hardly looks like a trial.](../article/assets/artifact-bridge-attempt-1.jpg)

Early Qwen attempt · A short bridge above a shallow stream hardly looks like a trial.

![Next attempt · There is height, but the bridge resembles a sturdy pedestrian crossing.](../article/assets/artifact-bridge-attempt-2.jpg)

Next attempt · There is height, but the bridge resembles a sturdy pedestrian crossing.

![Another version · A wide deck and substantial railings still look reassuringly solid.](../article/assets/artifact-bridge-attempt-3.jpg)

Another version · A wide deck and substantial railings still look reassuringly solid.

![Rope version · The materials change, but the deck and supports remain too substantial.](../article/assets/artifact-bridge-attempt-4.jpg)

Rope version · The materials change, but the deck and supports remain too substantial.

I only got the bridge I wanted after supplying photographs as references: a long suspended span, widely spaced boards and a pronounced sag. They helped communicate exactly what needed to look dangerous.

![Photographic reference I supplied · Widely spaced boards and rope construction. A real bridge photograph, not a film frame.](../article/assets/artifact-bridge-reference-1.jpg)

Photographic reference I supplied · Widely spaced boards and rope construction. A real bridge photograph, not a film frame.

![Second photographic reference I supplied · A long suspended span with a pronounced sag. A real bridge photograph, not project-generated imagery.](../article/assets/artifact-bridge-reference-2.jpg)

Second photographic reference I supplied · A long suspended span with a pronounced sag. A real bridge photograph, not project-generated imagery.

The references brought the scale and sense of danger I wanted, but new errors remained in the keyframe: rope railing on only one side, and three hands on the character—one holding the rope and two holding the rolled map. The agent missed them despite frequently regenerating other flawed images. I only noticed the extra hand near the end myself. By then I had started trusting Luna’s checks too much and was inspecting the results less carefully myself. At 00:56–00:58 it had already carried over into the final video. I left this example as a reminder to check both anatomy and the surrounding structure again after improving the composition.

![Bridge keyframe · An extra hand is already visible around the rolled map.](../article/assets/artifact-bridge-key.jpg)

Bridge keyframe · An extra hand is already visible around the rolled map.

There was a reason for that trust: Luna often spotted obvious failures on its own. For example, when creating an ending keyframe, the local model received the starting frame, an appearance reference for the character and a request to change his position. Instead of using the reference only to preserve his appearance, the model inserted it into the scene as a second character. Luna rejected that version. After seeing those checks work, both the agent and I found it easier to miss the extra hand in the bridge frame.

![Rejected keyframe · The appearance reference became a second character instead of helping reposition the original one.](../article/assets/artifact-reference-duplicate.jpg)

Rejected keyframe · The appearance reference became a second character instead of helping reposition the original one.

### Qwen missed the puzzle; GPT Image complicated the frames

I could not get suitable keyframes for trial three from Qwen: in my attempts it struggled with the perspective and the idea of the water puzzle itself. Below are early staging attempts and a later GPT Image frame. The camera angle, channel shapes, character position and mechanism changed between attempts.

![Early attempt · An almost frontal view of the character and puzzle.](../article/assets/artifact-puzzle-candidate-1.jpg)

Early attempt · An almost frontal view of the character and puzzle.

![Early attempt · An overhead view and square channel pieces.](../article/assets/artifact-puzzle-candidate-2.jpg)

Early attempt · An overhead view and square channel pieces.

![Early attempt · A different perspective, character position and water route.](../article/assets/artifact-puzzle-candidate-3.jpg)

Early attempt · A different perspective, character position and water route.

![Early attempt · The platform geometry and channel depth change.](../article/assets/artifact-puzzle-candidate-4.jpg)

Early attempt · The platform geometry and channel depth change.

![Early attempt · Another angle on interacting with a square piece.](../article/assets/artifact-puzzle-candidate-5.jpg)

Early attempt · Another angle on interacting with a square piece.

![Later GPT Image frame · Round discs and clearer staging, but a great deal of fine detail.](../article/assets/artifact-puzzle-candidate-6.jpg)

Later GPT Image frame · Round discs and clearer staging, but a great deal of fine detail.

GPT Image understood the scene better, but its images were overloaded with fine detail and visual noise. The keyframes differed from one another, and the resulting video lost facial detail and image stability. I tried adding a character reference at the video stage and then tried without it. I think manually cleaning up and matching the GPT Image keyframes might have improved these fragments. I did not test that approach.

### “Simulating” water with a local model

Trial three was the most demanding sequence. The water needed to flow, stop against a wrongly aligned channel, reach the next obstruction after one turn and eventually drive the wheel. But the model kept forgetting to animate the water: the flow stayed frozen even though the scene depended on its movement. One successful moment did emerge: in the clip below, the water advances along the channel after the disc turns correctly. In that fragment, MiniMax surprised me with how convincing the movement looked.

[Trial 3 · The correct first turn: water advances through disc A and stops inside disc B; the wheel remains still.](../article/assets/water-first-turn.mp4?raw=true)

The prompt also had to specify what stayed still: the wheel should not start turning just because there is water somewhere in the shot.

### Water flowing up a wall

The stream shifted in the solved-puzzle keyframe: the channel outlet sat below the point where water fed the wheel. The video model continued that geometry, sending the water uphill along the stone wall and into the wheel. It is less obvious in motion, but the frame sequence makes the broken physics clear. The successful first-disc turn above does not mean that the whole water sequence worked.

![Solved-puzzle keyframe · The height difference between the channel and wheel is already inconsistent.](../article/assets/artifact-water-key.jpg)

Solved-puzzle keyframe · The height difference between the channel and wheel is already inconsistent.

![02:23 · Before the second disc turns.](../article/assets/artifact-water-step-1.jpg)

02:23 · Before the second disc turns.

![02:24 · The disc changes position.](../article/assets/artifact-water-step-2.jpg)

02:24 · The disc changes position.

![02:25 · Water reaches the channel outlet.](../article/assets/artifact-water-step-3.jpg)

02:25 · Water reaches the channel outlet.

![02:25.2 · The channel ends below the wheel’s feed point.](../article/assets/artifact-water-step-4.jpg)

02:25.2 · The channel ends below the wheel’s feed point.

![02:25.4 · Water begins climbing the wall.](../article/assets/artifact-water-step-5.jpg)

02:25.4 · Water begins climbing the wall.

![02:25.7 · Water reaches the top of the stone projection.](../article/assets/artifact-water-step-6.jpg)

02:25.7 · Water reaches the top of the stone projection.

![02:26.1 · The flow and spray rise toward the wheel.](../article/assets/artifact-water-step-7.jpg)

02:26.1 · The flow and spray rise toward the wheel.

### The hourglass flip

At 02:34–02:36 the model failed to flip the hourglass convincingly: the glass deforms instead of following a clear rotation. The sand and mechanism were less successful than the good water movement or camera work. I left this fragment in the film as an example of an error.

![Starting state · Sand below, gates closed.](../article/assets/artifact-timer-before.jpg)

Starting state · Sand below, gates closed.

![Timer keyframe · Sand above, gates open. This shows the state after starting, not an intermediate rotation.](../article/assets/artifact-timer-after.jpg)

Timer keyframe · Sand above, gates open. This shows the state after starting, not an intermediate rotation.

![Actual last image in the video task · The character touches the bell; the sand is already above.](../article/assets/artifact-timer-bell.jpg)

Actual last image in the video task · The character touches the bell; the sand is already above.

![02:34–02:36 · An unconvincing intermediate hourglass state in the video.](../article/assets/artifact-timer-glitch.jpg)

02:34–02:36 · An unconvincing intermediate hourglass state in the video.

I checked the saved prompt.txt and media.json for scene09-start-v1. The prompt explicitly asks the glass to flip on horizontal side pivots after the bell, with the wooden stand fixed and the sand moving with the glass. The rotation instruction was therefore present. The actual inputs were the starting image and the bell-contact image, rather than the establish/timer pair shown above. Neither shows an intermediate rotation.

These materials suggest two possible difficulties: the model had to infer the rotation path between endpoint states, and the same 6.5 seconds also had to fit the bell, moving sand, opening gates and the character’s reaction. These are possible explanations rather than a proven diagnosis. A clearer intermediate frame and a separate short shot of the flip would be worth testing in another attempt.

[02:34–02:36.5 · Final-film excerpt showing the failed flip in motion.](../article/assets/artifact-hourglass.mp4?raw=true)

### Video-model speech becomes unintelligible

At 02:58–03:01 I left an example of failed speech in the film. In my generations the video model struggled with voices in languages other than English, producing unintelligible sounds instead of a clear line. I kept the moment as an example of that limitation. For intelligible Russian dialogue elsewhere, I used Drama 3.

[02:58–03:01 · Original final-film audio retained: the unintelligible speech is the point of this example.](../article/assets/artifact-speech.mp4?raw=true)

<a id="film"></a>

## Four minutes of local filmmaking

[Watch the film](../article/assets/film.mp4?raw=true)

Working cut v3 · 4:10.250 · Russian audio

<a id="story"></a>

## From a pirate dossier to a shooting star

The complete plot follows, including the gift and ending.

It began with a ninth birthday and a gift: a grey two-wheeled scooter. I wanted it to become the reward at the end of an adventure. In the original “Island of Nine Treasures”, the treasures represented qualities and wishes: courage, curiosity, ingenuity, speed, agility, persistence, loyal friends, luck and a big dream. Long generation times and a tight deadline led me to shorten the route to four trials. The title kept its connection to the ninth birthday.

Treasure Island inspired the pirate atmosphere and the mock-serious dossier. I made the dossier illustrated and used a photorealistic character based on photographic references for the other scenes.

### A ship, a folder and a map

A sailing ship approaches an island and its bay. Inside the cabin, a pirate places a personnel folder on a table. The dossier introduces a nine-year-old adventurer, and a stamp admits him to the crew. On deck, the photorealistic character receives a map and a mission: four trials. A boat brings him ashore; he checks the route and walks into the jungle.

![The character unfolding a map on the ship’s deck](../article/assets/map.jpg)

00:42 · Receiving the map. Even hair moving in the sea breeze helps sell the location.

### Trial one: courage

The first obstacle is a long suspension bridge above a deep valley. It sways, the camera circles around it to reveal the drop, and a plank cracks. The character reaches the opposite bank just in time. Only after the landing does the courage achievement appear.

![The character on a rope bridge above a forested valley](../article/assets/bridge.jpg)

01:04 · The bridge needed convincing height, unstable boards and movement.

### Trial two: curiosity

The trail reaches a wall of vines. The camera shows the dead end from the character’s viewpoint before he enters the shot. He looks around, scratches his head and notices a flashing shell on a sign. ‘Oh!’ He approaches and physically turns the signboard. The vines part at the same time, revealing a passage. He carries the map through it and earns the curiosity achievement.

![The character noticing a bright shell beside a blocked jungle path](../article/assets/shell.jpg)

01:31 · The sign must turn because the character moves it; the opening follows that action.

### Trial three: ingenuity

The passage leads to a stone platform with water channels, two rotating discs, a waterwheel and a closed door. I built the puzzle around the logic of a pipe-connecting game. The character puts the map down and tries a disc in the wrong direction. Turning the wheel by hand is no lasting solution either: the door opens while he works, then closes when he lets go to wipe away sweat.

He must connect the water’s route. After the first correct turn, the stream reaches the second obstacle. After the second, it reaches the wheel, drives it and holds the door open. The character can now leave the mechanism and walk through. The third achievement marks ingenuity.

![Water flowing between rotating stone discs toward a waterwheel](../article/assets/puzzle.jpg)

02:21 · Disc positions determine where the water can actually go.

### Trial four: speed

A bell starts a large hourglass and opens the distant gate. The character watches the sand while time is already running out. Then he puts away the map and takes off. The edit alternates between the run, the falling sand and the closing passage. He makes it through, catches his breath and earns the fourth achievement. All that remains is to reach the marked treasure.

![The character running toward a gate with an hourglass in the foreground](../article/assets/speed.jpg)

02:54 · A timed sprint toward the closing gate.

### The chest and a very unusual vessel

Above the bay, the character finds the chest, puts the map away and says, ‘There you are!’ He lifts the lid himself. Inside are the folded grey scooter and a helmet. The narrator introduces a new achievement in shipbuilding; a startled parrot wakes beside the chest and delivers a rehearsed pirate joke.

> ‘Two wheels, one handlebar, not a single cannon. But what speed!’

![The character opening a chest containing a scooter and helmet](../article/assets/gift.jpg)

03:16 · The character holds the lid; the parrot gives the reveal its punchline.

### A night-time descent and the birthday ending

I decided to end the story in the spirit of the Tomb Raider series: after finding the treasure, the character descends along a sloping zipline straight to the beach. The scooter goes into a case. In the final staging, the character holds the handle of a suspended trolley with both hands, replacing the earlier idea of using ice axes.

Day turns to night. The narrator tells the new captain to discover routes and remember his helmet as the character descends toward the bay. On the beach, now with helmet and scooter, the character watches the stars light up. A shooting star accompanies the final birthday wish.

![The character with a scooter beneath a starry sky and shooting star](../article/assets/stars.jpg)

04:06 · The adventure ends with a personal birthday greeting on the beach.

### About the material

I reconstructed this account from production chats, scene journals, workflows and the v3 timeline. Illustrations include film frames, original keyframes and crops I supplied; the captions distinguish them. Timecodes refer to the final assembly. Model comparisons, water motion, image degradation, speed and RAM figures are observations from my attempts rather than controlled benchmarks.

Music: Kevin MacLeod — Adventures in Adventureland, CC BY 4.0, edited and mixed with dialogue/effects. Ocean ambience: Joseph Sardin / BigSoundBank, CC0. Tools and models retain their upstream licenses.

[Credits](../CREDITS.md)
