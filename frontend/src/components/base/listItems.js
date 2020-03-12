import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import SubmitReportIcon from '@material-ui/icons/Send';
import CreditCardIcon from '@material-ui/icons/CreditCard';


export const mainListItems = (
    <div>
        <ListItem button>
            <ListItemIcon>
                <DashboardIcon />
            </ListItemIcon>
            <ListItemText primary="Dashboard" />
        </ListItem>
        <ListItem button>
            <ListItemIcon>
                <CreditCardIcon />
            </ListItemIcon>
            <ListItemText primary="Credit Card Benefits" />
        </ListItem>
        <ListItem button>
            <ListItemIcon>
                <SubmitReportIcon />
            </ListItemIcon>
            <ListItemText primary="Expense Submit" />
        </ListItem>
    </div>
);