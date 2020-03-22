import React, {useEffect, useState} from "react";
import {makeStyles, withStyles} from "@material-ui/core/styles";
import {Paper, TableBody, TableCell, TableContainer, TableRow} from "@material-ui/core";
import Table from "@material-ui/core/Table";
import {useSelector} from "react-redux";
import {axiosGet} from "../utils/axiosHelper";
import EnhancedTableHead from "../common/EnhancedTableHead";
import {getComparator, stableSort} from "../utils/tableSort";


const useStyles = makeStyles(theme => ({
    table: {
        minWidth: 650,
    }
}));


const StyledTableCell = withStyles(theme => ({
    head: {
        backgroundColor: theme.palette.common.black,
        color: theme.palette.common.white,
    },
    body: {
        fontSize: 14,
    }
}))(TableCell);


export default function CreditCardBenefit() {
    const classes = useStyles();
    const userAuth = useSelector(state => state.userAuth);
    const [benefits, setBenefits] = useState([]);
    const [order, setOrder] = useState('asc');
    const [orderBy, setOrderBy] = useState('reward');
    const headCells = [
        {id: 'reward',  numeric: false, label: 'Reward'},
        {id: 'name',    numeric: false, label: 'Name'},
        {id: 'bank',    numeric: false, label: 'Bank'},
        {id: 'owner',   numeric: false, label: 'Owner'},
        {id: 'xpoints', numeric: true, label: 'XPoints'},
        {id: 'start',   numeric: false, label: 'Start'},
        {id: 'end',     numeric: false, label: 'End'},
        {id: 'last4d',  numeric: false, label: 'Last4 Digits'},
    ];

    useEffect(() => {
        axiosGet("/api/budgetmgr/current-rewards/", userAuth.token)
            .then(res => {
                buildBenefitsData(res.data);
            }).catch(err => {
                console.error(`Failed to fetch current rewards, ${err}`);
            });
        // eslint-disable-next-line
    }, []);

    const buildBenefitsData = data => {
        const ret = [];
        // eslint-disable-next-line array-callback-return
        data.map(row => {
            ret.push({
                bank: row.account.institution.name,
                name: row.account.alias,
                owner: row.account.owner.name,
                reward: row.reward_type.name,
                xpoints: row.xpoints,
                start: row.start_time,
                end: row.end_time,
                last4digits: row.account.number.slice(-4),
            })
        });
        setBenefits(ret);
    };

    const handleRequestSort = (event, property) => {
        const isAsc = orderBy === property && order === 'asc';
        setOrder(isAsc ? 'desc' : 'asc');
        setOrderBy(property);
    };

    return (
        <TableContainer component={Paper}>
            <Table className={classes.table} aria-label="cc benfits">
                <EnhancedTableHead
                    order={order}
                    orderBy={orderBy}
                    onRequestSort={handleRequestSort}
                    headCells={headCells}
                />
                <TableBody>
                    {stableSort(benefits, getComparator(order, orderBy))
                        .map((row, index) => {
                            return (
                                <TableRow hover key={index}>
                                    <StyledTableCell>{row.reward}</StyledTableCell>
                                    <StyledTableCell>{row.name}</StyledTableCell>
                                    <StyledTableCell>{row.bank}</StyledTableCell>
                                    <StyledTableCell>{row.owner}</StyledTableCell>
                                    <StyledTableCell>{row.xpoints}</StyledTableCell>
                                    <StyledTableCell>{row.start}</StyledTableCell>
                                    <StyledTableCell>{row.end}</StyledTableCell>
                                    <StyledTableCell>{row.last4digits}</StyledTableCell>
                                </TableRow>
                            );
                        })
                    }
                </TableBody>
            </Table>
        </TableContainer>
    );
}