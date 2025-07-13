from otree.api import *

class Constants(BaseConstants):
    name_in_url = 'ball_drag_original'
    players_per_group = None
    num_rounds = 1
    total_balls = 10
    blue_multiplier = 0.05
    yellow_multiplier = 0.10

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    blue_balls = models.IntegerField(initial=0)
    yellow_balls = models.IntegerField(initial=0)
    total_earnings = models.FloatField()
    current_sum = models.FloatField()
    blue_total = models.FloatField()
    yellow_total = models.FloatField()
    blue_total = models.FloatField()
    yellow_total = models.FloatField()

    def calculate_earnings(self):
        self.total_earnings = (
            self.blue_balls * Constants.blue_multiplier +
            self.yellow_balls * Constants.yellow_multiplier
        )
    
    def calculate_sum(self):
        self.current_sum = self.total_earnings
        self.participant.vars['ball_drag_points'] = self.total_earnings

    
    

class Instructions(Page):
    pass
    

class BucketGame(Page):
    form_model = 'player'
    form_fields = ['blue_balls', 'yellow_balls']

    def error_message(self, values):
        if values['blue_balls'] + values['yellow_balls'] != Constants.total_balls:
            return f"The total number of balls must be {Constants.total_balls}."

    def before_next_page(self, timeout_happened = False):
        self.calculate_earnings()

class Results(Page):
    @staticmethod
    def vars_for_template(player):
        return {
            'earnings': f'€{player.total_earnings:.2f}',
            'blue_balls': player.blue_balls,
            'yellow_balls': player.yellow_balls,
            'blue_earnings': f'€{(player.blue_balls * Constants.blue_multiplier):.2f}',
            'yellow_earnings': f'€{(player.yellow_balls * Constants.yellow_multiplier):.2f}'
        }

page_sequence = [Instructions, BucketGame, Results]