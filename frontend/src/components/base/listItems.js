import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import SubmitReportIcon from '@material-ui/icons/Send';
import CreditCardIcon from '@material-ui/icons/CreditCard';
import ReceiptIcon from "@material-ui/icons/Receipt";
import {Link} from "react-router-dom";


export const mainListItems = (
    <React.Fragment>
        <ListItem button component={Link} to="/">
            <ListItemIcon>
                <DashboardIcon />
            </ListItemIcon>
            <ListItemText primary="Dashboard"/>
        </ListItem>
        <ListItem button component={Link} to="/ccbenefits">
            <ListItemIcon>
                <CreditCardIcon />
            </ListItemIcon>
            <ListItemText primary="Credit Card Benefits"/>
        </ListItem>
        <ListItem button component={Link} to="/expense-submit">
            <ListItemIcon>
                <SubmitReportIcon />
            </ListItemIcon>
            <ListItemText primary="Expense Submit"/>
        </ListItem>
        <ListItem button component={Link} to="/expense-overview">
            <ListItemIcon>
                <ReceiptIcon />
            </ListItemIcon>
            <ListItemText primary="Expense Overview"/>
        </ListItem>
    </React.Fragment>
);