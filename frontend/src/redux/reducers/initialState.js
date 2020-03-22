export const initialState = {
    auth: {
        username: "",
        isAuthenticated: process.env.NODE_ENV === 'production' ? null : true,
        token: "",
    }
};