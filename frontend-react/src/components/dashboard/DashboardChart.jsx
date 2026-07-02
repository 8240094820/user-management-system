import {
  Card,
  CardContent,
  Typography,
} from "@mui/material";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

function DashboardChart({
  admin,
  staff,
}) {

  const data = [
    {
      name: "Admin",
      value: admin,
    },
    {
      name: "Staff",
      value: staff,
    },
  ];

  const COLORS = [
    "#2563EB",
    "#16A34A",
  ];

  return (
    <Card>

      <CardContent>

        <Typography
          variant="h6"
          mb={2}
        >
          User Distribution
        </Typography>

        <ResponsiveContainer
          width="100%"
          height={300}
        >

          <PieChart>

            <Pie
              data={data}
              dataKey="value"
              outerRadius={100}
            >

              {data.map(
                (entry, index) => (

                  <Cell
                    key={index}
                    fill={COLORS[index]}
                  />

                )
              )}

            </Pie>

            <Tooltip />

          </PieChart>

        </ResponsiveContainer>

      </CardContent>

    </Card>
  );
}

export default DashboardChart;