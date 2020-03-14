import React from "react";
import {Redirect, Route} from "react-router-dom";
import {useSelector} from "react-redux";

export default function PrivateRoute({children, ...rest}) {
    const userAuth = useSelector(state => state.userAuth);

    return (
        <Route
            {...rest}
            render={() =>
                userAuth.isAuthenticated ? (
                    children
                ) : (
                    <Redirect to={{pathname: "/login"}}/>
                )
            }
        />
    );
};
