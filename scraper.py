{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "e2e82278-3499-4a48-9572-9122cd0ecdfc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import requests\n",
    "from bs4 import BeautifulSoup\n",
    "import sqlite3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "4d8de622-4ade-46ec-8b8e-6e683b844d20",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://github.com/MATaouk/aec_postcode_electorate_data_rerun\"\n",
    "response = requests.get(url)\n",
    "content = response.text\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "c17d54a6-daee-4b5a-b705-9548ce9e396a",
   "metadata": {},
   "outputs": [],
   "source": [
    "soup = BeautifulSoup(content, 'html.parser')\n",
    "data_elements = soup.find_all('div', class_='data_class')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c74210a7-bdcf-4d5b-950c-880349ea5081",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Connect to SQLite or create the database if it doesn't exist\n",
    "conn = sqlite3.connect('data.sqlite')\n",
    "cursor = conn.cursor()\n",
    "\n",
    "# Create a table if it doesn't already exist\n",
    "cursor.execute('''\n",
    "    CREATE TABLE IF NOT EXISTS data (\n",
    "        id INTEGER PRIMARY KEY AUTOINCREMENT,\n",
    "        column1 TEXT,\n",
    "        column2 TEXT\n",
    "    )\n",
    "''')\n",
    "\n",
    "# Insert the data\n",
    "for element in data_elements:\n",
    "    column1_value = element.find('span', class_='name').text\n",
    "    column2_value = element.find('span', class_='info').text\n",
    "    cursor.execute('INSERT INTO data (column1, column2) VALUES (?, ?)', (column1_value, column2_value))\n",
    "\n",
    "# Commit and close connection\n",
    "conn.commit()\n",
    "conn.close()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1387141c-b2ef-43cc-a456-bbc5c1db782c",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
