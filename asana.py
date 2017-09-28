#!/usr/bin/env python2
"""Interactions with Asana"""
import sys
import json
import requests
import os


class Asana:
    """Handle all of the Asana interactions"""
    base_url = "https://app.asana.com/api/1.0/"
    # Pull the export env variable and set equal to the api_key
    api_key = "Bearer " + os.environ['ASANA_ACCESS_TOKEN']

    def get_workspaces(self):
        """Return the list of workspaces"""
        endpoint = self.base_url + "workspaces"
        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", endpoint, headers=headers)
        response = response.json()
        return response

    def get_projects(self):
        """Return a list of Projects within Asana"""
        endpoint = self.base_url + "projects"
        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", endpoint, headers=headers)
        response = response.json()
        return response

    def get_id_from_input(self, input, search_term):
        """Return the ID from the given inputs"""
        ## Inputs can be Workspaces or Projects
        for term in input['data']:
            if search_term == term['name']:
                return term['id']
            else:
                return "No matches found! Please try again"

    def get_all_tasks_within_project(self, project_id):
        """Return a json object with all tasks"""
        endpoint = self.base_url + "projects/{}/tasks".format(project_id)
        headers = {
            'Authorization': self.api_key,
            'Content-Type': 'application/json'
        }
        response = requests.request("GET", endpoint, headers=headers)
        response = response.json()
        return response

    def count_return_values(self, json_object):
        """Return the count of json entries into the json_object"""
        amount_json_objects = 0

        for count in json_object['data']:
            amount_json_objects = amount_json_objects + 1

        return amount_json_objects

test = Asana()
# workspaces = test.get_workspaces()
projects =  test.get_projects()
project_id = test.get_id_from_input(projects, "University Work")
print project_id
data = test.get_all_tasks_within_project(project_id)
print test.count_return_values(data)