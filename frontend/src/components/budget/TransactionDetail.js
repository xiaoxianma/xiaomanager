import React, {useEffect, useState} from "react";
import {Link, useParams} from "react-router-dom";
import {makeStyles} from "@material-ui/core/styles";
import {useSelector} from "react-redux";
import {axiosGet} from "../utils/axiosHelper";
import ChildPageBase from "../common/ChildPageBase";
import Card from "@material-ui/core/Card";
import CardHeader from "@material-ui/core/CardHeader";
import CardContent from "@material-ui/core/CardContent";
import TableContainer from "@material-ui/core/TableContainer";
import Table from "@material-ui/core/Table";
import TableCell from "@material-ui/core/TableCell";
import TableBody from "@material-ui/core/TableBody";
import TableRow from "@material-ui/core/TableRow";
import Button from "@material-ui/core/Button";
import teal from '@material-ui/core/colors/teal';


const useStyles = makeStyles(theme => ({
    table: {
        border: "1px solid"
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
        backgroundColor: teal[500],
        '&:hover': {
            backgroundColor: teal[700]
        }
    }
}));

export default function TransactionDetail() {
    const classes = useStyles();
    const {id} = useParams();
    const userAuth = useSelector(state => state.userAuth);
    const [transactionDetail, setTransactionDetail] = useState(null);
    const [accountId, setAccountId] = useState(null);
    const [paymentInfo, setPaymentInfo] = useState(null);

    useEffect(() => {
        axiosGet(`/api/budgetmgr/transactions/${id}/`, userAuth.token)
            .then(res => {
                setTransactionDetail(res.data);
                setAccountId(res.data.account);
            })
            .catch(err => {
                console.error(`Failed to fetch transaction detail with id=${id}, ${err}`);
            });
    }, [userAuth.token, id]);

    useEffect(() => {
        if (accountId) {
            axiosGet(`/api/budgetmgr/accounts/${accountId}/`, userAuth.token)
                .then(res => {
                    setPaymentInfo(res.data);
                })
                .catch(err => {
                    console.error(`Failed to fetch account detail with id=${accountId}, ${err}`);
                });
        }
    }, [userAuth.token, accountId]);

    if (transactionDetail === null || paymentInfo === null) {
        return null;
    } else {
        const payment = `${paymentInfo.owner.name}|${paymentInfo.institution.name}|${paymentInfo.account_type.name}|${paymentInfo.alias}`.replace(/\|$/, '');
        return (
            <ChildPageBase>
                <Card>
                    <CardHeader title="Transaction Detail"/>
                    <CardContent>
                        <TableContainer>
                            <Table className={classes.table}>
                                <TableBody>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>ID</TableCell>
                                        <TableCell>{transactionDetail.id}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Amount</TableCell>
                                        <TableCell>{transactionDetail.amount}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Payment</TableCell>
                                        <TableCell>{payment}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Expense Category</TableCell>
                                        <TableCell>{transactionDetail.expense_type_name}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Transaction Date</TableCell>
                                        <TableCell>{transactionDetail.transaction_date}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Merchant Name</TableCell>
                                        <TableCell>{transactionDetail.merchant.name}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Merchant City</TableCell>
                                        <TableCell>{transactionDetail.merchant.city}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Merchant Country</TableCell>
                                        <TableCell>{transactionDetail.merchant.country}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Coupon</TableCell>
                                        <TableCell>{transactionDetail.coupon}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Tags</TableCell>
                                        <TableCell>{transactionDetail.tags}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Notes</TableCell>
                                        <TableCell>{transactionDetail.notes}</TableCell>
                                    </TableRow>
                                    <TableRow>
                                        <TableCell className={classes.firstColumn}>Create Time</TableCell>
                                        <TableCell>{transactionDetail.create_time}</TableCell>
                                    </TableRow>
                                </TableBody>
                            </Table>
                        </TableContainer>
                    </CardContent>
                    <Link to="/expense-submit" className={classes.link}>
                        <Button fullWidth variant="contained" className={classes.button}>New Expense</Button>
                    </Link>
                </Card>
            </ChildPageBase>
        );
    }
};
