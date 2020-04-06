import React, {useEffect, useState} from "react";
import {makeStyles} from "@material-ui/core/styles";
import {TextField} from "@material-ui/core";
import InputAdornment from "@material-ui/core/InputAdornment";
import Divider from "@material-ui/core/Divider";
import MenuItem from "@material-ui/core/MenuItem";
import Icon from "@material-ui/core/Icon";
import Button from "@material-ui/core/Button";
import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import {axiosGet, axiosPost} from "../utils/axiosHelper";
import {useSelector} from "react-redux";
import {ascendingComparator, sleep} from "../utils/funcUntil";
import ChildPageBase from "../common/ChildPageBase";
import {useHistory} from "react-router-dom";


const useStyles = makeStyles(theme => ({
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
    const history = useHistory();
    const userAuth = useSelector(state => state.userAuth);
    const [payments, setPayments] = useState([]);
    const [expenseCategories, setExpenseCategories] = useState([]);
    const [countries, setCountries] = useState([]);
    const [snackbarOpen, setSnackbarOpen] = useState(false);
    const [submitSuccess, setSubmitSuccess] = useState(null);
    const [transactionId, setTransactionId] = useState(null);
    // expense attributes
    const [amount, setAmount] = useState("");
    const [paymentId, setPaymentId] = useState("");
    const [expenseCategoryId, setExpenseCategoryId] = useState("");
    const [transactionDate, setTransactionDate] = useState(new Date().toISOString().slice(0, 10));
    const [merchantName, setMerchantName] = useState("");
    const [merchantCity, setMerchantCity] = useState("chicago");
    const [merchantCountry, setMerchantCountry] = useState("US");
    const [coupon, setCoupon] = useState("");
    const [tags, setTags] = useState("");
    const [notes, setNotes] = useState("");
    // input error status
    const [amountErr, setAmountErr] = useState(false);
    const [paymentIdErr, setPaymentIdErr] = useState(false);
    const [expenseCategoryIdErr, setExpenseCategoryIdErr] = useState(false);
    const [transactionDateErr, setTransactionDateErr] = useState(false);
    const [merchantNameErr, setMerchantNameErr] = useState(false);
    const [merchantCityErr, setMerchantCityErr] = useState(false);
    const [merchantCountryErr, setMerchantCountryErr] = useState(false);

    useEffect(() => {
        axiosGet("/api/budgetmgr/accounts/", userAuth.token)
            .then(res => {
                buildPaymentsData(res.data);
            })
            .catch(err => {
                console.error(`Failed to fetch current payments, ${err}`);
            });
        axiosGet("/api/budgetmgr/expense-types/", userAuth.token)
            .then(res => {
                buildExpenseCategoriesData(res.data);
            })
            .catch(err => {
                console.error(`Failed to fetch current expense types, ${err}`);
            });
        axiosGet("/api/budgetmgr/countries/", userAuth.token)
            .then(res => {
                buildCountriesData(res.data);
            })
            .catch(err => {
                console.error(`Failed to fetch countries list, ${err}`);
            });
    }, [userAuth.token]);

    useEffect(() => {
        if (transactionId) {
            sleep(1500).then(() => {
                history.push(`/transaction-detail/${transactionId}`);
            });
        }
    }, [history, transactionId]);

    const buildCountriesData = data => {
        const ret = data.map(row => {
            return {id: row.id, value: row.value};
        });
        ret.sort((a, b) => ascendingComparator(a, b, 'value'));
        setCountries(ret);
    };

    const buildPaymentsData = data => {
        const ret = data.map(row => {
            const value = `${row.owner.name}|${row.institution.name}|${row.account_type.name}|${row.alias}`.replace(/\|$/, '');
            return {id: row.id, value: value};
        });
        ret.sort((a, b) => ascendingComparator(a, b, 'value'));
        setPayments(ret);
    };

    const buildExpenseCategoriesData = data => {
        const ret = data.map(row => {
            return {id: row.id, value: row.name};
        });
        ret.sort((a, b) => ascendingComparator(a, b, 'value'));
        setExpenseCategories(ret);
    };

    const validateSubmitFields = () => {
        setAmountErr(!Boolean(amount));
        setPaymentIdErr(!Boolean(paymentId));
        setExpenseCategoryIdErr(!Boolean(expenseCategoryId));
        setTransactionDateErr(!Boolean(transactionDate));
        setMerchantNameErr(!Boolean(merchantName));
        setMerchantCityErr(!Boolean(merchantCity));
        setMerchantCountryErr(!Boolean(merchantCountry));
        return Boolean(amount && paymentId && expenseCategoryId && transactionDate && merchantName && merchantCity && merchantCountry);
    };

    const handleSubmit = () => {
        if (!validateSubmitFields()) return;
        const payload = {
            amount: parseFloat(amount),
            account: paymentId,
            expense_type: expenseCategoryId,
            merchant: {
                name: merchantName,
                city: merchantCity,
                country: merchantCountry,
            },
            transaction_date: transactionDate,
            coupon: coupon ? coupon : null,
            tags: tags ? tags.split(",") : [],
            notes: notes,
        };
        axiosPost("/api/budgetmgr/transactions/", payload, userAuth.token)
            .then(res => {
                setSubmitSuccess(true);
                setTransactionId(res.data.id);
            })
            .catch(err => {
                console.error(`Failed to submit expense, ${err}`);
                setSubmitSuccess(false);
            });
        setSnackbarOpen(true);
    };

    const handleSnackbarClose = (event, reason) => {
        if (reason === "clickaway") return;
        setSnackbarOpen(false);
        setSubmitSuccess(null);
    };

    return (
        <ChildPageBase>
            <div>
                <h3>Please enter your expense below</h3>
            </div>
            <div>
                <TextField
                    required
                    fullWidth
                    id="amount"
                    label="Amount"
                    value={amount}
                    onChange={event => setAmount(event.target.value)}
                    error={amountErr}
                    type="number"
                    className={classes.textField}
                    variant="outlined"
                    InputProps={{
                        startAdornment: <InputAdornment position="start">$</InputAdornment>,
                        inputProps: {min: 0, step: 0.5},
                    }}
                />
                <TextField
                    fullWidth
                    select
                    id="payment"
                    label="Payment"
                    value={paymentId}
                    onChange={event => setPaymentId(event.target.value)}
                    error={paymentIdErr}
                    className={classes.textField}
                    variant="outlined"
                >
                    {payments.map((option) => (
                        <MenuItem key={option.id} value={option.id}>
                            {option.value}
                        </MenuItem>
                    ))}
                </TextField>
                <TextField
                    fullWidth
                    select
                    id="expense-type"
                    label="Expense Category"
                    value={expenseCategoryId}
                    onChange={event => setExpenseCategoryId(event.target.value)}
                    error={expenseCategoryIdErr}
                    className={classes.textField}
                    variant="outlined"
                >
                    {expenseCategories.map((option) => (
                        <MenuItem key={option.id} value={option.id}>
                            {option.value}
                        </MenuItem>
                    ))}
                </TextField>
                <TextField
                    required
                    fullWidth
                    id="transaction-date"
                    label="Transaction Date"
                    value={transactionDate}
                    onChange={event => setTransactionDate(event.target.value)}
                    error={transactionDateErr}
                    type="date"
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
                    value={merchantName}
                    onChange={event => setMerchantName(event.target.value)}
                    error={merchantNameErr}
                    className={classes.textField}
                    variant="outlined"
                />
                <TextField
                    required
                    fullWidth
                    id="merchant-city"
                    label="City"
                    value={merchantCity}
                    onChange={event => setMerchantCity(event.target.value)}
                    error={merchantCityErr}
                    className={classes.textField}
                    variant="outlined"
                />
                <TextField
                    required
                    fullWidth
                    select
                    id="Country"
                    label="Merchant Country"
                    value={merchantCountry}
                    onChange={event => setMerchantCountry(event.target.value)}
                    error={merchantCountryErr}
                    className={classes.textField}
                    variant="outlined"
                >
                    {countries.map((option, index) => (
                        <MenuItem key={index} value={option.id}>
                            {option.value}
                        </MenuItem>
                    ))}
                </TextField>
                <Divider className={classes.divider}/>
                <TextField
                    fullWidth
                    id="coupon"
                    label="Coupon"
                    value={coupon}
                    onChange={event => setCoupon(event.target.value)}
                    className={classes.textField}
                    type="number"
                    variant="outlined"
                    InputProps={{
                        startAdornment: <InputAdornment position="start">$</InputAdornment>,
                        inputProps: {min: 0, step: 0.5},
                    }}
                />
                <TextField
                    fullWidth
                    id="tags"
                    label="Tags"
                    value={tags}
                    onChange={event => setTags(event.target.value)}
                    helperText="please use , separate tags"
                    className={classes.textField}
                    variant="outlined"
                />
                <TextField
                    fullWidth
                    multiline
                    id="notes"
                    label="Notes"
                    value={notes}
                    onChange={event => setNotes(event.target.value)}
                    className={classes.textField}
                    variant="outlined"
                />
                <Button
                    fullWidth
                    onClick={handleSubmit}
                    variant="contained"
                    color="secondary"
                    style={{marginTop: 10}}
                    endIcon={<Icon>send</Icon>}
                >
                    Submit
                </Button>
                <div>
                    <Snackbar open={snackbarOpen} autoHideDuration={5000} onClose={handleSnackbarClose}
                              style={{width: "100%"}}>
                        {submitSuccess === null ? null : submitSuccess === true ?
                            <MuiAlert variant="filled" severity="success" style={{width: "100%"}}>A new expense is
                                posted successfully! Redirecting to the expense detail Page...</MuiAlert> :
                            <MuiAlert variant="filled" severity="error" style={{width: "100%"}}>Your expense is failed
                                to post!</MuiAlert>
                        }
                    </Snackbar>
                </div>
            </div>
        </ChildPageBase>
    );
}