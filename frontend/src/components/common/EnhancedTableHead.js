import React from "react";
import TableCell from "@material-ui/core/TableCell";
import TableSortLabel from "@material-ui/core/TableSortLabel";
import TableHead from "@material-ui/core/TableHead";
import TableRow from "@material-ui/core/TableRow";
import {makeStyles, withStyles} from "@material-ui/core/styles";


const StyledTableCell = withStyles(theme => ({
    head: {
        backgroundColor: theme.palette.common.black,
    },
}))(TableCell);


const StyledTableSortLabel = withStyles(theme => ({
    root: {
        color: theme.palette.common.white,
        "&:hover": {
            color: theme.palette.common.white,
        },
        '&$active': {
            color: theme.palette.common.white,
        },
    },
    active: {},
    icon: {
        color: 'inherit !important'
    },
}))(TableSortLabel);


const useStyles = makeStyles(theme => ({
    visuallyHidden: {
        border: 0,
        clip: 'rect(0 0 0 0)',
        height: 1,
        margin: -1,
        overflow: 'hidden',
        padding: 0,
        position: 'absolute',
        top: 20,
        width: 1,
    },
}));

export default function EnhancedTableHead(props) {
    const classes = useStyles();
    const {order, orderBy, onRequestSort, headCells} = props;

    const createSortHandler = property => event => {
        onRequestSort(event, property);
    };

    return (
        <TableHead>
            <TableRow>
                {headCells.map(headCell => (
                    <StyledTableCell
                        key={headCell.id}
                        sortDirection={orderBy === headCell.id ? order : false}
                    >
                        <StyledTableSortLabel
                            active={orderBy === headCell.id}
                            direction={orderBy === headCell.id ? order : 'asc'}
                            onClick={createSortHandler(headCell.id)}
                        >
                            {headCell.label}
                            {orderBy === headCell.id ? (
                                <span className={classes.visuallyHidden}>
                                    {order === 'desc' ? 'sorted descending' : 'sorted ascending'}
                                </span>
                            ) : null}
                        </StyledTableSortLabel>
                    </StyledTableCell>
                ))}
            </TableRow>
        </TableHead>
    );
}