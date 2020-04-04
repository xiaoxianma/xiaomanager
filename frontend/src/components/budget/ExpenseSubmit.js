import React from "react";
import {makeStyles} from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import {APP_BAR_HEIGHT} from "../utils/globalParams";
import {TextField} from "@material-ui/core";
import InputAdornment from "@material-ui/core/InputAdornment";
import Container from "@material-ui/core/Container";
import grey from "@material-ui/core/colors/grey";
import Divider from "@material-ui/core/Divider";
import MenuItem from "@material-ui/core/MenuItem";


const useStyles = makeStyles(theme => ({
    root: {
        display: 'flex',
        flexWrap: 'wrap',
        height: `calc(100% - ${APP_BAR_HEIGHT}px)`,
    },
    container: {
        backgroundColor: grey[200],
    },
    textField: {
        marginTop: theme.spacing(1),
        marginBottom: theme.spacing(1),
        backgroundColor: theme.palette.common.white,
    },
    divider: {
        marginBottom: theme.spacing(1),
    }
}));

export default function ExpenseSubmit() {
    const classes = useStyles();
    const payments = [{id: 1, value: 1}, {id: 2, value: 2}];
    return (
        <Paper className={classes.root}>
            <Container maxWidth="sm" className={classes.container}>
                <div>
                    <h3>Please enter your expense below</h3>
                </div>
                <div>
                    <TextField
                        required
                        fullWidth
                        id="amount"
                        label="Amount"
                        className={classes.textField}
                        variant="outlined"
                        InputProps={{startAdornment: <InputAdornment position="start">$</InputAdornment>}}
                    />
                    <TextField
                        required
                        fullWidth
                        select
                        id="payment"
                        label="Payment"
                        className={classes.textField}
                        variant="outlined"
                    >
                        {payments.map((option) => (
                            <MenuItem key={option.id} value={option.value}>
                                {option.value}
                            </MenuItem>
                        ))}
                    </TextField>
                    <TextField
                        required
                        fullWidth
                        select
                        id="expense-type"
                        label="Expense Category"
                        className={classes.textField}
                        variant="outlined"
                    >
                        {payments.map((option) => (
                            <MenuItem key={option.id} value={option.value}>
                                {option.value}
                            </MenuItem>
                        ))}
                    </TextField>
                    <TextField
                        required
                        fullWidth
                        id="transaction-date"
                        label="Transaction Date"
                        type="date"
                        defaultValue={new Date().toISOString().slice(0, 10)}
                        className={classes.textField}
                        variant="outlined"
                    />
                    <div>
                        <span style={{fontSize: 14}}>Merchant</span>
                        <Divider/>
                    </div>
                    <TextField
                        required
                        fullWidth
                        id="merchant-name"
                        label="Name"
                        className={classes.textField}
                        variant="outlined"
                    />
                    <TextField
                        required
                        fullWidth
                        defaultValue="chicago"
                        id="merchant-city"
                        label="City"
                        className={classes.textField}
                        variant="outlined"
                    />
                    <TextField
                        required
                        fullWidth
                        defaultValue="US"
                        id="Country"
                        label="Merchant Country"
                        className={classes.textField}
                        variant="outlined"
                    />
                    <Divider className={classes.divider}/>
                    <TextField
                        fullWidth
                        id="coupon"
                        label="Coupon"
                        className={classes.textField}
                        variant="outlined"
                        InputProps={{startAdornment: <InputAdornment position="start">$</InputAdornment>}}
                    />
                    <TextField
                        fullWidth
                        id="tags"
                        label="Tags"
                        helperText="please use , separate tags"
                        className={classes.textField}
                        variant="outlined"
                    />
                    <TextField
                        fullWidth
                        multiline
                        id="notes"
                        label="Notes"
                        className={classes.textField}
                        variant="outlined"
                    />
                </div>
            </Container>
        </Paper>
    );
}