import asyncio
import math
import discord
from discord.ext import commands
from cogs.challonge_driver import Driver


class Match:

    instance = None

    def __init__(self, ctx: commands.Context, interval: int) -> None:
        self.ctx = ctx
        self.message_ids = {}
        self.has_finished = False
        self.interval = interval

        # TODO: Challounge username, API_KEY
        self.creds = (
            "bunxyz", "zmIG44cw40om3SSY4OuVi8Qg2ZuhboBu1AL7Z4zd")
        self.driver = Driver(username=self.creds[0], api_key=self.creds[1])
        self.tournament_id = self.driver.getTournamentIDs()[0]

    def fetch_data(self):
        matches = filter(lambda x: x['match']['state'] !=
                         "pending", self.driver.getMatches(self.tournament_id))
        participants = self.driver.getParticipants(self.tournament_id)
        return matches, participants

    def prepare_embeds(self, matches, participants):
        matches_embed = {}
        for match in matches:
            details = match['match']
            p1 = list(filter(
                lambda x: x['participant']['id'] == details['player1_id'], participants))[0]
            p2 = list(filter(
                lambda x: x['participant']['id'] == details['player2_id'], participants))[0]
            embed = discord.Embed(title=str(p1['participant']['name']) + " vs " + str(
                p2['participant']['name']), color=0xff0000)

            if details['state'] == 'complete':
                embed.add_field(
                    value=' - '.join(details['scores_csv'].split('-')), name="Score")
            else:
                embed.add_field(
                    value="NOT YET STARTED" if details['state'] == 'open' else "ON GOING", name="Score")
            matches_embed[details['id']] = embed
        return matches_embed

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

    async def send_embeds(self):
        matches, participants = self.fetch_data()
        embeds = self.prepare_embeds(matches, participants)
        for id in embeds:
            if not self.message_ids.get(id, False):
                self.message_ids[id] = await self.ctx.send(embed=embeds[id])
            else:
                await self.message_ids[id].edit(embed=embeds[id])

        to_delete = []
        for id in self.message_ids:
            if id not in embeds:
                await self.message_ids[id].delete()
                to_delete.append(id)

        for id in to_delete:
            del self.message_ids[id]


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
            await self.send_embeds()
            await asyncio.sleep(self.interval)

    async def stop(self):
        to_delete = []
        for id in self.message_ids:
            await self.message_ids[id].delete()
            to_delete.append(id)

        for id in to_delete:
            del self.message_ids[id]

        self.has_finished = True

    # @staticmethod
    # def get_instance(ctx : commands.Context, interval : int):
    #     if Match.instance:
    #         return Match.instance
    #     else:
    #         Match.instance = Match(ctx, interval)
    #         return Match.instance
