import React from 'react';
import Header from "./base/Header";
import {BrowserRouter as Router, Route, Switch} from "react-router-dom";
import Login from "./base/Login";
import PrivateRoute from "./common/PrivateRoute";
import DashBoard from "./budget/Dashboard";
import CreditCardBenefits from "./budget/CreditCardBenefits";
import NotFound from "./common/NotFound";
import {makeStyles} from "@material-ui/core/styles";
import CssBaseline from "@material-ui/core/CssBaseline";
import ExpenseSubmit from "./budget/ExpenseSubmit";


const useStyle = makeStyles(theme => ({
    root: {
        display: 'flex',
    },
    content: {
        flexGrow: 1,
        height: '100vh',
        overflow: 'auto',
    },
    appBarSpacer: theme.mixins.toolbar,
}));


export default function App() {
    const classes = useStyle();

    return (
        <div className={classes.root}>
            <Router>
                <CssBaseline/>
                <Header/>
                <main className={classes.content}>
                    <div className={classes.appBarSpacer}/>
                    <Switch>
                        <Route exact path="/login"><Login/></Route>
                        <PrivateRoute exact path="/"><DashBoard/></PrivateRoute>
                        <PrivateRoute exact path="/ccbenefits"><CreditCardBenefits/></PrivateRoute>
                        <PrivateRoute exact path="/expense-submit"><ExpenseSubmit/></PrivateRoute>
                        <Route path="*"><NotFound/></Route>
                    </Switch>
                </main>
            </Router>
        </div>
    );
};

