import random
import math
import game_framework
from BehaviorTree import BehaviorTree, SelectorNode, SequenceNode, LeafNode
from pico2d import *
import main_state

# zombie Run Speed
PIXEL_PER_METER = (10.0 / 0.3)  # 10 pixel 30 cm
RUN_SPEED_KMPH = 10.0  # Km / Hour
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

# zombie Action Speed
TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 10


animation_names = ['Attack', 'Dead', 'Idle', 'Walk']


class Zombie:
    images = None

    def load_images(self):
        if Zombie.images == None:
            Zombie.images = {}
            for name in animation_names:
                Zombie.images[name] = [load_image("./zombiefiles/female/"+ name + " (%d)" % i + ".png") for i in range(1, 11)]

    def __init__(self):
        # positions for origin at top, left

        self.target_x, self.target_y = None, None
        self.x, self.y = random.randint(200, 1000), random.randint(200, 1000)

        self.load_images()
        self.font = load_font('ENCR10B.TTF', 25)
        self.dir = random.random()*2*math.pi # random moving direction
        self.speed = 0
        self.timer = 1.0  # change direction every 1 sec when wandering
        self.frame = 0
        self.hp = 100
        self.build_behavior_tree()

    def calculate_current_position(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % FRAMES_PER_ACTION
        self.x += self.speed * math.cos(self.dir) * game_framework.frame_time
        self.y += self.speed * math.sin(self.dir) * game_framework.frame_time
        self.x = clamp(50, self.x, 1280 - 50)
        self.y = clamp(50, self.y, 1024 - 50)

    def wander(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()
        self.timer -= game_framework.frame_time

        if self.timer < 0:
            self.timer += 1.0
            self.dir = random.random() * 2 * math.pi

        return BehaviorTree.SUCCESS
        pass

    def determine_next_position_to_player(self):
        # fill here
        boy = main_state.get_boy()
        distance = (boy.x - self.x) ** 2 + (boy.y - self.y) ** 2

        if distance < (PIXEL_PER_METER * 8) ** 2:
            if self.is_more_hp_than_player() is True:
                self.dir = math.atan2(boy.y - self.y, boy.x - self.x)
                return BehaviorTree.SUCCESS
            else:
                self.speed = 0
                return BehaviorTree.FAIL
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def determine_next_position_to_escape(self):
        boy = main_state.get_boy()
        distance = (boy.x - self.x) ** 2 + (boy.y - self.y) ** 2

        if distance < (PIXEL_PER_METER * 8) ** 2:
            self.dir = math.atan2(self.y - boy.y, self.x - boy.x)
            return BehaviorTree.SUCCESS
        else:
            self.speed = 0
            return BehaviorTree.FAIL
        pass

    def move_to_player(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        return BehaviorTree.SUCCESS
        pass

    def is_more_hp_than_player(self):
        boy = main_state.get_boy()
        if boy.hp < self.hp:
            return True
        else:
            return False
        pass

    def get_next_position(self):
        # fill here
        self.target_x, self.target_y = self.patrol_positions[self.patrol_order % len(self.patrol_positions)]
        self.patrol_order += 1
        self.dir = math.atan2(self.target_y - self.y, self.target_x - self.x)

        return BehaviorTree.SUCCESS
        pass

    def move_to_target(self):
        # fill here
        self.speed = RUN_SPEED_PPS
        self.calculate_current_position()

        distance = (self.target_x - self.x)**2 + (self.target_y - self.y)**2

        if distance < PIXEL_PER_METER**2:
            return BehaviorTree.SUCCESS
        else:
            return BehaviorTree.RUNNING
        pass

    def find_ball(self):

        balls = main_state.get_balls()
        distance = None
        for ball in balls:
            distance = (self.x - ball.x) ** 2 + (self.y - ball.y) ** 2
            if distance < (PIXEL_PER_METER * 5) ** 2:
                self.dir = math.atan2(ball.y - self.y, ball.x - self.x)
                return BehaviorTree.SUCCESS
            else:
                pass

        self.speed = 0
        return BehaviorTree.FAIL

        pass

    def build_behavior_tree(self):
        # fill here
        # 1 - wander
        # wander_node = LeafNode("Wander", self.wander)
        # self.bt = BehaviorTree(wander_node)

        # 2 - patrol
        # get_next_position_node = LeafNode("Get Next Position", self.get_next_position)
        # move_to_target_node = LeafNode("Move to Target", self.move_to_target)
        # patrol_node = SequenceNode("Patrol")
        # patrol_node.add_children(get_next_position_node, move_to_target_node)
        # self.bt = BehaviorTree(patrol_node)

        # 3 - Chase
        # find_player_node = LeafNode("Find Player", self.find_player)
        # move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        # chase_node = SequenceNode("Chase")
        # chase_node.add_children(find_player_node, move_to_player_node)
        # self.bt = BehaviorTree(chase_node)

        # 4 - Chase and Wander
        # wander_node = LeafNode("Wander", self.wander)
        # find_player_node = LeafNode("Find Player", self.find_player)
        # move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        # chase_node = SequenceNode("Chase")
        # chase_node.add_children(find_player_node, move_to_player_node)
        # wander_chase_node = SelectorNode("WanderChase")
        # wander_chase_node.add_children(chase_node, wander_node)
        # self.bt = BehaviorTree(wander_chase_node)

        determine_next_position_to_player_node = \
            LeafNode("Determine next position to player", self.determine_next_position_to_player)
        move_to_player_node = LeafNode("Move to Player", self.move_to_player)
        chase_node = SequenceNode("Chase Player")
        chase_node.add_children(determine_next_position_to_player_node, move_to_player_node)

        determine_next_position_to_escape_node = \
            LeafNode("Determine next position to escape", self.determine_next_position_to_escape)
        move_to_escape_node = LeafNode("Move to escape", self.move_to_player)
        run_away_node = SequenceNode("Run away player")
        run_away_node.add_children(determine_next_position_to_escape_node, move_to_escape_node)

        chase_or_escape_node = SelectorNode("Chase or Escape")
        chase_or_escape_node.add_children(chase_node, run_away_node)

        # ball chase
        find_ball_node = LeafNode("Find Ball", self.find_ball)
        move_to_ball_node = LeafNode("Move to Ball", self.move_to_player)

        chase_ball_node = SequenceNode("Chase Ball")
        chase_ball_node.add_children(find_ball_node, move_to_ball_node)

        wander_node = LeafNode("Wander", self.wander)

        root_node = SelectorNode("Root")
        root_node.add_children(chase_or_escape_node, chase_ball_node, wander_node)

        self.bt = BehaviorTree(root_node)

        # chase_player_node = SequenceNode("Chase Player")

        # run_away_from_the_player = SequenceNode("Run away from the player")
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50

    def update(self):
        # fill here
        self.bt.run()
        pass

    def draw(self):
        if math.cos(self.dir) < 0:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].composite_draw(0, 'h', self.x, self.y, 100, 100)
        else:
            if self.speed == 0:
                Zombie.images['Idle'][int(self.frame)].draw(self.x, self.y, 100, 100)
            else:
                Zombie.images['Walk'][int(self.frame)].draw(self.x, self.y, 100, 100)

        self.font.draw(self.x - 50, self.y + 60, 'Hp:%3d' % self.hp, (255, 0, 0))
        pass

    def handle_event(self, event):
        pass

