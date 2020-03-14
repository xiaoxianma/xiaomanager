import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './components/App';
import {Provider} from "react-redux";
import {Route, Switch, BrowserRouter as Router} from 'react-router-dom';
import store from "./redux/store";
import * as serviceWorker from './serviceWorker';
import Login from "./components/base/Login";
import PrivateRoute from "./components/common/PrivateRoute";


ReactDOM.render(
    <Provider store={store}>
        <Router>
            <Switch>
                <Route path="/login">
                    <Login/>
                </Route>
                <PrivateRoute exact path="/">
                    <App/>
                </PrivateRoute>
            </Switch>
        </Router>
    </Provider>,
    document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
