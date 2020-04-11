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
        marginBottom: theme.spacing(3),
        width: 80,
    }
}));

export default function ExpenseOverview() {
    const classes = useStyles();
    const userAuth = useSelector(state => state.userAuth);
    const [transactions, setTransactions] = useState([]);
    const [transactionDeltaDays, setTransactionDeltaDays] = useState(30);

    useEffect(() => {
        const minDate = new Date(new Date().setDate(new Date().getDate() - transactionDeltaDays)).toISOString();
        axiosGet(`/api/budgetmgr/transactions/?min_date=${minDate}`, userAuth.token)
            .then(res => {
                buildTransactionsData(res.data);
            })
            .catch(err => {
                console.error(`Failed to fetch transaction list, ${err}`);
            })
    }, [userAuth.token, transactionDeltaDays]);

    const buildTransactionsData = (data) => {
        const ret = data.map(row => {
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
    };

    if (transactions === null) {
        return null;
    } else {
        return (
            <ChildPageBase maxWidth="md">
                <Card className>
                    <CardHeader title="Transactions"/>
                    <CardContent>
                        <TextField
                            required
                            id="last_days"
                            label="Last days"
                            value={transactionDeltaDays}
                            type="number"
                            className={classes.textField}
                            onChange={event => setTransactionDeltaDays(parseInt(event.target.value))}
                        />
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