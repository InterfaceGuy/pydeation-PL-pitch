from pydeation.imports import *


class RelationshipToStories(Scene):

    def construct(self):

        earth = Earth(color=BLUE)
        money = Money(color=BLUE)
        health = Health(color=BLUE)
        symbols = Group(earth, money, health)
        stories = Text("stories", x=200, color=BLUE)
        symbols.position_on_circle(at_bottom=health)
        civilization = Human(perspective="portrait",
                             posture="standing", color=RED)
        stories_lens = Text("stories", y=50)

        self.play(Draw(civilization))
        self.play(Draw(symbols))
        self.play(Connect(civilization, target=symbols,
                          grow_from="middle", direction="bidirectional"))
        self.wait()
        self.play(UnCreate(money, health))
        self.play(Move(earth, x=200, y=0), Move(civilization, x=-200, y=0))

        stories_lens.attach_to(earth.connection, direction="top")

        self.play(Write(stories_lens))
        self.wait()
        self.play(Morph(stories_lens, stories), FadeOut(earth))
        self.wait()
        self.play(UnCreate(stories, civilization))


class PhysicalCampfire():

    def __init__(self):

        self.circle = Circle()
        self.left_human = Human(
            perspective="profile_left", posture="sitting")
        self.right_human = Human(
            perspective="profile_right", posture="sitting")
        self.humans = Group(left_human, right_human)
        self.fire = Fire(glow=True)
        self.symbol = ProjectLiminality()


class Campfires(Scene):

    def construct(self):

        main_campfire = PhysicalCampfire()
        campfires = Group(main_campfire)
        for i in range(5):
            campfire = PhysicalCampfire()
            campfires.add(campfire)

        campfires.position_on_circle()

        walking_paths = campfires.create_connections(
            count=6, turbulence=True, style="dashed")

        self.play(Create(main_campfire))
        self.play(main_campfire.dialectic())
        self.play(main_campfire.sand_talk())
        self.play(self.zoom_out(), Create(campfires))
        self.play(Draw(walking_paths))
        self.play(UnCreate(main_campfire, campfires, walking_paths))


class FromP2PToBroadcast(Scene):

    def construct(self):
        pass


class PLSymbol(Scene):

    def construct(self):

        symbol = ProjectLiminality(text=True)

        self.play(Create(symbol))
        self.play(UnCreate(symbol))


class EssenceOfLogos(Scene):

    def construct(self):

        ancient_dialogos = PhysicalCampfire()
        ancient_interlogos = Group(*[Circle() for i in range(6)])
        ancient_interlogos.position_on_circle()

        # place circle center out of frame
        campfires.position_on_circle(y=-100)

        ancient_interlogos = campfires.create_connections(
            count=6, turbulence=True, style="dashed")

        modern_monologos = YouTube()
        modern_dialogos = DigitalCampfire()
        modern_interlogos = campfires.create_connections()

        self.play(Create(campfires))
        self.play(
            Transform(ancient_dialogos.symbol, x=-100, y=100, relative=False),
            Highlight(ancient_dialogos.symbol))
        self.play(
            Move(ancient_dialogos.humans, ancient_dialogos.fire, x=100, y=100),
            Highlight(ancient_dialogos.humans, ancient_dialogos.fire))
        self.play(
            Transform(campfires, scale=1 / 4, y=100),
            Highlight(campfires))
        self.play(Morph(ancient_dialogos.symbol, modern_monologos))
        self.play(Morph(ancient_dialogos.fire, modern_dialogos))
        self.play(Morph(ancient_interlogos, modern_interlogos))
        self.play(self.focus_on(modern_dialogos.right_screen))


class UnBundling(Scene):

    def construct(self):

        dialogos_node_left = DiaLogosNode()
        dialogos_node_right = DiaLogosNode()
        dialogos_nodes = Group(dialogos_node_left, dialogos_node_right)
        monologos_node = MonoLogosNode()
        nodes = Group(dialogos_nodes, monologos_node)
        nodes.position_on_circle(start_with=monologos_node)

        # conversation beacon
        beacon = Antenna()
        beacon.attach_to(monologos_node, position="top")

        self.play(Create(dialogos_node_left))
        self.play(
            Create(monologos_node),
            Connect(dialogos_node_left, target=monologos_node))
        self.play(Create(dialogos_node_right))
        self.play(Connect(dialogos_node_right, target=monologos_node))
        self.play(Create(beacon))
        self.play(UnCreate(nodes, beacon))


class DigitalSandTalk(Scene):

    def construct(self):

        chat_partner = Human(perspective="portrait", posture="sitting")
        chat_window = Window()
        sand_talk_window = Window()
        windows = Group(chat_window, sand_talk_window)
        monologos_node = MonoLogosNode()

        self.play(Create(windows, chat_partner, mode="linear"))
        self.play(Create(monologos_node))
        # applies the UnCreate animator to all visible elements
        self.play(Clear())


class ReBundling(Scene):

    def construct(self):

        dialogos_node = DiaLogosnode(y=100)
        monologos_nodes = Group(*[MonoLogosNode() for i in range(3)])
        monologos_nodes.position_on_line(
            start=(-100, -100, 0), stop=(100, -100, 0))
        nodes = Group(monologos_nodes, dialogos_node)

        self.play(Create(dialogos_node))
        self.play(Create(monologos_nodes, mode="linear"))
        self.play(Connect(monologos_nodes, target=dialogos_node, mode="linear"))
        self.play(UnCreate(dialogos_node, monologos_nodes))


class MappingLogos(Scene):
    # show a growing liminal web using x-particles

    def construct(self):
        pass


class Implications(Scene):

    def construct(self):
        pass
