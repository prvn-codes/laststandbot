import asyncio
import math
import discord
from discord.ext import commands
from cogs.challonge_driver import Driver


class Match:

    instance = None

    def __init__(self, ctx: commands.Context, interval: int) -> None:
        self.ctx = ctx
        self.message = None
        self.has_finished = False
        self.interval = interval

        # TODO: Challounge username, API_KEY
        self.creds = (
            "", "")
        self.driver = Driver(username=self.creds[0], api_key=self.creds[1])
        self.tournament_id = self.driver.getTournamentIDs()[0]

    def fetch_data(self):
        matches = filter(lambda x: x['match']['state'] !=
                         "pending", self.driver.getMatches(self.tournament_id))
        participants = self.driver.getParticipants(self.tournament_id)
        return matches, participants

    def prepare_embed(self, title: str, description: str, color: int, matches, participants):
        matches_embed = discord.Embed(
            title=title, description=description, color=color)
        for match in matches:
            details = match['match']
            p1 = list(filter(
                lambda x: x['participant']['id'] == details['player1_id'], participants))[0]
            p2 = list(filter(
                lambda x: x['participant']['id'] == details['player2_id'], participants))[0]
            if details['state'] == 'complete':
                matches_embed.add_field(name=str(p1['participant']['name']) + " vs " + str(
                    p2['participant']['name']), value=' - '.join(details['scores_csv'].split('-')), inline=False)
            else:
                matches_embed.add_field(name=str(p1['participant']['name']) + " vs " + str(
                    p2['participant']['name']), value="NOT YET STARTED" if details['state'] == 'open' else "ON GOING", inline=False)

        return matches_embed

    async def send_embed(self):
        matches, participants = self.fetch_data()
        embed = self.prepare_embed(
            "Matches", "Last Stand Match History", 0xff0000, matches, participants)
        if not self.message:
            self.message = await self.ctx.send(embed=embed)
        else:
            await self.message.edit(embed=embed)

    async def run(self):
        while not self.has_finished:
            await self.send_embed()
            await asyncio.sleep(self.interval)

    async def stop(self):
        self.has_finished = True

    # @staticmethod
    # def get_instance(ctx : commands.Context, interval : int):
    #     if Match.instance:
    #         return Match.instance
    #     else:
    #         Match.instance = Match(ctx, interval)
    #         return Match.instance