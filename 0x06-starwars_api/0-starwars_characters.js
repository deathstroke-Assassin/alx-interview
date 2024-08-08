#!/usr/bin/node

const axios = require('axios');

async function getswchar(movie_id) {
	"""Fetches and prints characters from a Star Wars movie."""
	try {
		const { data: movieData } = await axios.get('https://swapi-api.alx-tools.com/films/${movie_id}');
		const characters = movieData.characters;
		for (const characterUrl of characters) {
		      const { data: characterData } = await axios.get(characterUrl);
		      console.log(characterData.name);
	    } catch (error) {
        console.error(error);
    }
}

const movie_id = process.argv[2];
getswchar(movie_id);
