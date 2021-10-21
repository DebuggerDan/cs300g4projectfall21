# CS 300 - Group (#4) Project: ChocAn [Section: Database] - Fall 2021
# Christopher Juncker, Justin Greever, Samantha Zeigler, Tori Anderson, Naya Mairena, Ian Guy, Dan Jang


# Create a database for storing information about the company, the customers, and the services provided.

import numpy as np
import os
import sys
import json
import logging
import functools
from datetime import date time, timedelta
from collections import namedtuple
from typing import List, Dict, Tuple, Optional, Union

class Database():
    def __init__(self):
        pass

    def __init__(self, db_file: str = 'database.json'):
        self.db_file = db_file
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.INFO)
        self.logger.info('Database initialized')

    def __enter__(self):
        self.logger.info('Database entered')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.logger.info('Database exited')

    def load_database(self) -> None:
        """
        Loads the database from the file.
        """
        self.logger.info('Loading database')
        with open(self.db_file, 'r') as f:
            self.database = json.load(f)
        self.logger.info('Database loaded')

    def save_database(self) -> None:
        """
        Saves the database to the file.
        """
        self.logger.info('Saving database')
        with open(self.db_file, 'w') as f:
            json.dump(self.database, f)
        self.logger.info('Database saved')

    def get_database(self) -> Dict:
        """
        Returns the database.
        """
        return self.database

    def get_member_id(self) -> int:
        """
        Returns the next available member id.
        """
        self.logger.info('Getting next member id')
        if 'member_id' in self.database:
            return self.database['member_id']
        else:
            return 0

    def get_provider_id(self) -> int:
        """
        Returns the next available provider id.
        """
        self.logger.info('Getting next provider id')
        if 'provider_id' in self.database:
            return self.database['provider_id']
        else:
            return 0

    def get_service_id(self) -> int:
        """
        Returns the next available service id.
        """
        self.logger.info('Getting next service id')
        if 'service_id' in self.database:
            return self.database['service_id']
        else:
            return 0

    def get_member_info(self, member_id: int) -> Dict:
        """
        Returns the member information for the given member id.
        """
        self.logger.info('Getting member info for member id: %d', member_id)
        return self.database['members'][member_id]

    def get_provider_info(self, provider_id: int) -> Dict:
        """
        Returns the provider information for the given provider id.
        """
        self.logger.info('Getting provider info for provider id: %d', provider_id)
        return self.database['providers'][provider_id]
    
    def get_service_info(self, service_id: int) -> Dict:
        """
        Returns the service information for the given service id.
        """
        self.logger.info('Getting service info for service id: %d', service_id)
        return self.database['services'][service_id]

    def add_member(self, member_info: Dict) -> None:
        """
        Adds a member to the database.
        """
        self.logger.info('Adding member: %s', member_info)
        member_id = self.get_member_id()
        self.database['members'][member_id] = member_info
        self.database['member_id'] = member_id + 1
        self.save_database()

    def add_provider(self, provider_info: Dict) -> None:
        """
        Adds a provider to the database.
        """
        self.logger.info('Adding provider: %s', provider_info)
        provider_id = self.get_provider_id()
        self.database['providers'][provider_id] = provider_info
        self.database['provider_id'] = provider_id + 1
        self.save_database()
    
    def add_service(self, service_info: Dict) -> None:
        """
        Adds a service to the database.
        """
        self.logger.info('Adding service: %s', service_info)
        service_id = self.get_service_id()
        self.database['services'][service_id] = service_info
        self.database['service_id'] = service_id + 1
        self.save_database()

    def update_member(self, member_id: int, member_info: Dict) -> None:
        """
        Updates the member information for the given member id.
        """
        self.logger.info('Updating member: %d', member_id)
        self.database['members'][member_id] = member_info
        self.save_database()

    def update_provider(self, provider_id: int, provider_info: Dict) -> None:
        """
        Updates the provider information for the given provider id.
        """
        self.logger.info('Updating provider: %d', provider_id)
        self.database['providers'][provider_id] = provider_info
        self.save_database()

    def update_service(self, service_id: int, service_info: Dict) -> None:
        """
        Updates the service information for the given service id.
        """
        self.logger.info('Updating service: %d', service_id)
        self.database['services'][service_id] = service_info
        self.save_database()

    def delete_member(self, member_id: int) -> None:
        """
        Deletes the member information for the given member id.
        """
        self.logger.info('Deleting member: %d', member_id)
        del self.database['members'][member_id]
        self.save_database()

    def delete_provider(self, provider_id: int) -> None:
        """
        Deletes the provider information for the given provider id.
        """
        self.logger.info('Deleting provider: %d', provider_id)
        del self.database['providers'][provider_id]
        self.save_database()

    def delete_service(self, service_id: int) -> None:
        """
        Deletes the service information for the given service id.
        """
        self.logger.info('Deleting service: %d', service_id)
        del self.database['services'][service_id]
        self.save_database()

    def get_member_services(self, member_id: int) -> List[int]:
        """
        Returns a list of service ids for the given member id.
        """
        self.logger.info('Getting member services for member id: %d', member_id)
        return self.database['members'][member_id]['services']

    def get_provider_services(self, provider_id: int) -> List[int]:
        """
        Returns a list of service ids for the given provider id.
        """
        self.logger.info('Getting provider services for provider id: %d', provider_id)
        return self.database['providers'][provider_id]['services']

    def add_member_service(self, member_id: int, service_id: int) -> None:
        """
        Adds a service to the member's services.
        """
        self.logger.info('Adding member service: %d, %d', member_id, service_id)
        self.database['members'][member_id]['services'].append(service_id)
        self.save_database()

    def add_provider_service(self, provider_id: int, service_id: int) -> None:
        """
        Adds a service to the provider's services.
        """
        self.logger.info('Adding provider service: %d, %d', provider_id, service_id)
        self.database['providers'][provider_id]['services'].append(service_id)
        self.save_database()

    def remove_member_service(self, member_id: int, service_id: int) -> None:
        """
        Removes a service from the member's services.
        """
        self.logger.info('Removing member service: %d, %d', member_id, service_id)
        self.database['members'][member_id]['services'].remove(service_id)
        self.save_database()
    
    def remove_provider_service(self, provider_id: int, service_id: int) -> None:
        """
        Removes a service from the provider's services.
        """
        self.logger.info('Removing provider service: %d, %d', provider_id, service_id)
        self.database['providers'][provider_id]['services'].remove(service_id)
        self.save_database()
