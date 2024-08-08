const axios = require('axios').default;

async function getUsers() {
    try {
        const responce = await axios.get('https://swapi-api.alx-tools.com/');
        console.log(responce);
    } catch (error) {
        console.error(error);
    }
}
getUsers()