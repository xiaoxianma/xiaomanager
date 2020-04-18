import React, {useEffect, useState} from "react";
import {makeStyles} from "@material-ui/core/styles";
import cyan from "@material-ui/core/colors/cyan";
import {axiosGet} from "../utils/axiosHelper";
import {useSelector} from "react-redux";
import {descendingComparator} from "../utils/funcUntil";
import ChildPageBase from "../common/ChildPageBase";
import {TextField} from "@material-ui/core";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import Table from "@material-ui/core/Table";
import Card from "@material-ui/core/Card";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import TableCell from "@material-ui/core/TableCell";
import TableBody from "@material-ui/core/TableBody";
import {Link} from "react-router-dom";
import NavigateNextIcon from "@material-ui/icons/NavigateNext";
import IconButton from "@material-ui/core/IconButton";
import moment from "moment";

const useStyles = makeStyles(theme => ({
    table: {
        border: "1px solid",
    },
    firstColumn: {
        fontWeight: "bold",
        borderRight: "1px solid"
    },
    link: {
        textDecoration: "none",
    },
    button: {
        color: theme.palette.common.white,
        backgroundColor: cyan[200],
        '&:hover': {
            backgroundColor: cyan[300]
        }
    },
    textField: {
        marginBottom: theme.spacing(2),
        marginRight: theme.spacing(2),
        width: 250,
    },
    summaryStats: {
        marginBottom: theme.spacing(2),
        borderSpacing: 0,
        borderRight: "thin solid grey",
        borderBottom: "thin solid grey",
    },
    summaryStatsBorder: {
        borderLeft: "thin solid grey",
        borderTop: "thin solid grey",
        paddingLeft: theme.spacing(2),
        paddingRight: theme.spacing(2),
    }
}));

export default function ExpenseOverview() {
    const classes = useStyles();
    const userAuth = useSelector(state => state.userAuth);
    const [transactions, setTransactions] = useState([]);
    const [fromDate, setFromDate] = useState(moment().subtract(30, 'days').format('YYYY-MM-DD'));
    const [toDate, setToDate] = useState(moment().format('YYYY-MM-DD'));
    const [totalExpense, setTotalExpense] = useState();
    const [totalTransactionCount, setTotalTransactionCount] = useState();

    useEffect(() => {
        const minDate = moment(fromDate, 'YYYY-MM-DD').format();
        const maxDate = moment(toDate, 'YYYY-MM-DD').format();
        axiosGet(`/api/budgetmgr/transactions/?min_date=${minDate}&max_date=${maxDate}`, userAuth.token)
            .then(res => {
                buildTransactionsData(res.data);
            })
            .catch(err => {
                console.error(`Failed to fetch transaction list, ${err}`);
            })
    }, [userAuth.token, fromDate, toDate]);

    const buildTransactionsData = (data) => {
        let expense = 0;
        let transactionCount = 0;
        const ret = data.map(row => {
            expense += row.amount;
            transactionCount += 1;
            return {
                id: row.id,
                date: row.transaction_date,
                description: row.merchant.name,
                category: row.expense_type_name,
                amount: row.amount,
            }
        });
        ret.sort((a, b) => descendingComparator(a, b, 'date'));
        setTransactions(ret);
        setTotalExpense(expense);
        setTotalTransactionCount(transactionCount);
    };

    if (transactions === null) {
        return null;
    } else {
        return (
            <ChildPageBase maxWidth="md">
                <Card>
                    <CardHeader title="Transactions"/>
                    <CardContent>
                        <TextField
                            id="transaction-min-date"
                            className={classes.textField}
                            label="From"
                            value={fromDate}
                            onChange={event => setFromDate(event.target.value)}
                            type="date"
                            variant="outlined"
                        />
                        <TextField
                            id="transaction-max-date"
                            className={classes.textField}
                            label="To"
                            value={toDate}
                            onChange={event => setToDate(event.target.value)}
                            type="date"
                            variant="outlined"
                        />
                        <table className={classes.summaryStats}>
                            <tr>
                                <th className={classes.summaryStatsBorder}>Expense($)</th>
                                <th className={classes.summaryStatsBorder}>Transactions</th>
                            </tr>
                            <tr className={classes.summaryStatsBorder}>
                                <td className={classes.summaryStatsBorder}>{totalExpense}</td>
                                <td className={classes.summaryStatsBorder}>{totalTransactionCount}</td>
                            </tr>
                        </table>
                        <Table className={classes.table} size="small">
                            <TableHead>
                                <TableRow>
                                    <TableCell>Date</TableCell>
                                    <TableCell>Description</TableCell>
                                    <TableCell>Category</TableCell>
                                    <TableCell>Amount</TableCell>
                                    <TableCell>Detail</TableCell>
                                </TableRow>
                            </TableHead>
                            <TableBody>
                                {transactions.map((row, index) => {
                                    const transactDetailUrl = `/transaction-detail/${row.id}`;
                                    return (
                                        <TableRow hover key={index}>
                                            <TableCell>{row.date}</TableCell>
                                            <TableCell>{row.description}</TableCell>
                                            <TableCell>{row.category}</TableCell>
                                            <TableCell>{row.amount}</TableCell>
                                            <TableCell>
                                                <Link to={transactDetailUrl} className={classes.link}>
                                                    <IconButton className={classes.button} component="span">
                                                        <NavigateNextIcon/>
                                                    </IconButton>
                                                </Link>
                                            </TableCell>
                                        </TableRow>
                                    );
                                })}
                            </TableBody>
                        </Table>
                    </CardContent>
                </Card>
            </ChildPageBase>
        );
    }
}