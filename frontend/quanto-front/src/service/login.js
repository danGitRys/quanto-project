const CLIENT_ID = 'sb-sap-btp-auth-setup!t217413';
const CLIENT_SECRET = '+CruGoEV+BalzEHXyL2mmJlFqHw=';
const AUTH_URL = 'https://3ac97b83trial.authentication.us10.hana.ondemand.com/oauth/token';
import ClientOAuth2 from 'client-oauth2';

const serverAuth = new ClientOAuth2({
    clientId: CLIENT_ID,
    clientSecret: CLIENT_SECRET,
    accessTokenUri: AUTH_URL,
    authorizationGrants: ['*'],
})
// console.log(CLIENT_ID,CLIENT_SECRET,AUTH_URL)
export const AuthService = {
    async login(email, password) {
        console.log("Test")
        return serverAuth.owner
            .getToken(email, password)
            .then(user => { console.log(user.accessToken); return user.accessToken })
    },
    logout() {
        TokenStorage.signOut();
        window.location.reload(false);
    }
}