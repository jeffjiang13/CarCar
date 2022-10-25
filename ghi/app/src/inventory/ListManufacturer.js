import React from 'react';

function ListManufacturer() {
    const [data, setData] = React.useState([]);
    React.useEffect(()=> {
        const url = "http://localhost:8100/api/manufacturers/";
        fetch(url)
        .then((response)=> response.json())
        .then((json)=> setData(json['manufacturers']))
        .catch((error)=> console.log(error));
    }, []);

    React.useEffect(()=> {
}, [data]);

    return (
        <div>
            <p></p>
            <h2>Manufacturers</h2>
            <table className="table">
                <thead>
                    <tr>
                        <th>Name</th>
                    </tr>
                </thead>
                <tbody>
                    {data.map(manufacturer => {
                        return (
                            <tr key={manufacturer.id}>
                                <td>{manufacturer.name}</td>
                            </tr>
                        );
                    })}
                </tbody>
            </table>
        </div>
    );
}

export default ListManufacturer;